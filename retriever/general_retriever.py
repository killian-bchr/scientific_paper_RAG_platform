from typing import Dict, List, Tuple

import numpy as np
from numpy import ndarray
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from database.session import get_session
from database.tables import PaperORM
from exceptions import InvalidQuery
from helpers.utils import Utils


class GeneralRetriever:
    def __init__(self, papers: List[PaperORM]):
        self.papers = papers
        self.paper_ids = [p.id for p in papers]

        self.is_empty = len(papers) == 0

        self.title_vectorizer = TfidfVectorizer(stop_words="english")
        self.abstract_vectorizer = TfidfVectorizer(stop_words="english")

        if not self.is_empty:
            self.title_matrix = self.title_vectorizer.fit_transform(
                [p.title for p in papers]
            )
            self.abstract_matrix = self.abstract_vectorizer.fit_transform(
                [p.abstract for p in papers]
            )
        else:
            self.title_matrix = None
            self.abstract_matrix = None

    def encode_query_to_vector(self, query: str) -> Tuple[csr_matrix, csr_matrix]:
        if not query or not query.strip():
            raise InvalidQuery("Query must not be empty.")

        if self.is_empty:
            return None, None

        return (
            self.title_vectorizer.transform([query]),
            self.abstract_vectorizer.transform([query]),
        )

    def compute_title_score(
        self,
        query_title: csr_matrix,
    ) -> ndarray:
        if self.is_empty:
            return np.zeros(len(self.paper_ids))

        return cosine_similarity(
            query_title,
            self.title_matrix,
        ).flatten()

    def compute_abstract_score(
        self,
        query_abstract: csr_matrix,
    ) -> ndarray:
        if self.is_empty:
            return np.zeros(len(self.paper_ids))

        return cosine_similarity(
            query_abstract,
            self.abstract_matrix,
        ).flatten()

    def compute_scores(self, query: str) -> Dict[int, float]:
        query_title, query_abstract = self.encode_query_to_vector(query)

        title_scores = self.compute_title_score(query_title)
        abstract_scores = self.compute_abstract_score(query_abstract)

        final_scores = title_scores + 0.8 * abstract_scores

        return {
            paper_id: score for paper_id, score in zip(self.paper_ids, final_scores)
        }

    def top_k_papers(
        self,
        query: str,
        k: int,
    ) -> List[int]:
        scores = self.compute_scores(query)
        return sorted(scores, key=scores.get, reverse=True)[:k]

    def retrieve_top_papers(self, query: str, k: int = 10) -> List[PaperORM]:
        top_papers = self.top_k_papers(query, k)
        with get_session() as session:
            result = [Utils.fecth_paper_by_id(session, p_id) for p_id in top_papers]

        return result
