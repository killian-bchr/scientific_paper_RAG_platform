from typing import List, Optional

from sqlalchemy.orm import Session

from backend.database.repositories import PaperRepository
from backend.domain.retriever import HybridRetriever
from backend.models import PaperRanked


class SearchService:
    @staticmethod
    def search_papers(
        session: Session,
        query: str,
        paper_ids: Optional[List[int]] = None,
        top_k_papers: int = 10,
        top_k_chunks: int = 10,
        chunk_relevance_threshold: float = 0.5,
    ) -> List[PaperRanked]:
        papers = PaperRepository.fetch_papers_by_ids(session, paper_ids)
        if not papers:
            return []

        retriever = HybridRetriever(papers)

        return retriever.retrieve(
            query,
            top_k_papers,
            top_k_chunks,
            chunk_relevance_threshold,
        )
