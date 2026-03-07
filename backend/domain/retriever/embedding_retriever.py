from typing import List

import numpy as np
from numpy import ndarray
from sklearn.metrics.pairwise import cosine_similarity

from backend.core.config import Config
from backend.core.exceptions import InvalidPaperId, InvalidQuery
from backend.database.repositories import ChunkRepository
from backend.database.session import get_session
from backend.database.tables import ChunkORM, PaperORM
from backend.domain.retriever.base import BaseRetriever
from backend.models import ChunkRanked


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

    def fetch_embeddings_by_paper_ids(
        self,
        paper_ids: List[int],
        chunks: List[ChunkORM],
    ) -> List[ndarray]:
        for p_id in paper_ids:
            if p_id not in self.paper_ids:
                raise InvalidPaperId(f"Paper: {p_id} doesn't match any paper selected")

        if not chunks or len(chunks) == 0:
            return np.empty((0, self.model.get_sentence_embedding_dimension()))

        return np.vstack([c.embedding for c in chunks])

    def retrieve_relevant_chunks(
        self,
        query: str,
        threshold: float = 0.5,
    ) -> List[ChunkRanked]:

        query_vect = self.encode_query_to_vector(query)

        with get_session() as session:
            chunks = ChunkRepository.fetch_chunks_by_paper_ids(session, self.paper_ids)

        embeddings = self.fetch_embeddings_by_paper_ids(self.paper_ids, chunks)

        scores = cosine_similarity(query_vect, embeddings).flatten()

        results = []

        for chunk, score in zip(chunks, scores):
            if score >= threshold:
                chunk_ranked = ChunkRanked(chunk=chunk, score=float(score))
                results.append(chunk_ranked)

        return results
