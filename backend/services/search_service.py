from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from backend.database.repositories import PaperRepository
from backend.database.tables import ChunkORM, PaperORM
from backend.domain.retriever import HybridRetriever


class SearchService:
    @staticmethod
    def search_papers(
        session: Session,
        query: str,
        paper_ids: Optional[List[int]] = None,
        k: int = 10,
    ) -> List[Tuple[PaperORM, float]]:
        papers = PaperRepository.fetch_papers_by_ids(session, paper_ids)
        if not papers:
            return []

        retriever = HybridRetriever(papers)

        return retriever.retrieve_top_papers_with_scores(query, k)

    @staticmethod
    def retrieve_chunks(
        session: Session,
        query: str,
        paper_ids: Optional[List[int]] = None,
        k: int = 10,
        threshold: float = 0.6,
    ) -> List[Tuple[ChunkORM, float]]:
        papers = PaperRepository.fetch_papers_by_ids(session, paper_ids)
        if not papers:
            return []

        retriever = HybridRetriever(papers)

        return retriever.retrieve_relevant_chunks(query, k, threshold)
