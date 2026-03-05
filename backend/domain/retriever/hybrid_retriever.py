from typing import Dict, List, Tuple

from backend.database.tables import ChunkORM, PaperORM
from backend.domain.retriever.base import BaseRetriever
from backend.domain.retriever.embedding_retriever import EmbeddingRetriever
from backend.domain.retriever.tfidf_retriever import TfidfRetriever


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

    def retrieve_relevant_chunks(
        self,
        query: str,
        top_k: int = 10,
        threshold: float = 0.6,
    ) -> List[Tuple[ChunkORM, float]]:
        return self.embedding_retriever.retrieve_relevant_chunks(
            query, top_k, threshold
        )
