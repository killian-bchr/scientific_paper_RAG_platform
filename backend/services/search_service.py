from typing import List, Optional

from sqlalchemy.orm import Session

from backend.core.date_utils import DateUtils
from backend.database.repositories import PaperRepository
from backend.domain.retriever import HybridRetriever
from backend.models import PaperRanked


class SearchService:
    @staticmethod
    def search_papers(
        session: Session,
        query: str,
        domain_id: Optional[int] = None,
        category_id: Optional[int] = None,
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
        top_k_papers: int = 10,
        top_k_chunks: int = 10,
        chunk_relevance_threshold: float = 0.5,
    ) -> List[PaperRanked]:
        start_date, end_date = DateUtils.compute_start_and_end_date(
            start_year, end_year
        )

        papers = PaperRepository.fetch_filtered_papers(
            session=session,
            domain_id=domain_id,
            category_id=category_id,
            start_date=start_date,
            end_date=end_date,
        )

        if not papers:
            return []

        retriever = HybridRetriever(papers)

        return retriever.retrieve(
            query,
            top_k_papers,
            top_k_chunks,
            chunk_relevance_threshold,
        )
