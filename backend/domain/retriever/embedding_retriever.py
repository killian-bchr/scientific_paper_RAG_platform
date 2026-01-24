from typing import Dict, List

import numpy as np
from numpy import ndarray
from retriever.base import BaseRetriever
from sklearn.metrics.pairwise import cosine_similarity

from backend.database.repositories import ChunkRepository
from backend.database.session import get_session
from backend.database.tables import PaperORM
from config import Config
from exceptions import InvalidPaperId, InvalidQuery


class EmbeddingRetriever(BaseRetriever):
    def __init__(self, papers: List[PaperORM]):
        super().__init__(papers)

        self.model = Config.EMBEDDING_MODEL

    def encode_query_to_vector(self, query: str) -> ndarray:
        if not query or not query.strip():
            raise InvalidQuery("Query must not be empty.")

        if self.is_empty:
            return None

        return self.model.encode(query, normalize_embeddings=True).reshape(1, -1)

    def fetch_embeddings_by_paper_id(self, paper_id: int) -> List[ndarray]:
        if paper_id not in self.paper_ids:
            raise InvalidPaperId(f"Paper: {paper_id} doesn't match any paper selected")

        with get_session() as session:
            chunks = ChunkRepository.fetch_chunks_by_paper_id(session, paper_id)

        if not chunks or len(chunks) == 0:
            return np.empty((0, self.model.get_sentence_embedding_dimension()))

        return np.vstack([c.embedding for c in chunks])

    def compute_score_by_paper(
        self,
        paper_id: int,
        query_vect: ndarray,
    ) -> float:
        embeddings = self.fetch_embeddings_by_paper_id(paper_id)

        if embeddings.shape[0] == 0:
            return 0.0

        scores = cosine_similarity(query_vect, embeddings).flatten()
        return scores.max()

    def compute_scores(self, query: str) -> Dict[int, float]:
        query_vect = self.encode_query_to_vector(query)

        return {
            paper_id: self.compute_score_by_paper(paper_id, query_vect)
            for paper_id in self.paper_ids
        }
