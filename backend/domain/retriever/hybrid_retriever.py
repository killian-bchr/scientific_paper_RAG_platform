from typing import Dict, List

from retriever.base import BaseRetriever
from retriever.embedding_retriever import EmbeddingRetriever
from retriever.tfidf_retriever import TfidfRetriever

from backend.database.tables import PaperORM


class HybridRetriever(BaseRetriever):
    def __init__(
        self,
        papers: List[PaperORM],
        alpha: float = 0.5,
    ):
        super().__init__(papers)

        self.tfidf_retriever = TfidfRetriever(papers)
        self.embedding_retriever = EmbeddingRetriever(papers)
        self.alpha = alpha

    def compute_scores(self, query: str) -> Dict[int, float]:
        tfidf_scores = self.tfidf_retriever.compute_scores(query)
        embedding_scores = self.embedding_retriever.compute_scores(query)

        final_scores = {}
        for paper_id in self.paper_ids:
            final_scores[paper_id] = self.alpha * tfidf_scores.get(paper_id, 0.0) + (
                1 - self.alpha
            ) * embedding_scores.get(paper_id, 0.0)

        return final_scores
