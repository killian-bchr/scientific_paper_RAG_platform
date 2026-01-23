from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from database.tables import PaperORM
from helpers.utils import Utils
from retriever import HybridRetriever


class SearchService:
    @staticmethod
    def search_papers(
        session: Session,
        query: str,
        paper_ids: Optional[List[int]] = None,
        k: int = 10,
    ) -> List[Tuple[PaperORM, float]]:
        papers = Utils.fetch_papers_by_ids(session, paper_ids)
        if not papers:
            return []

        retriever = HybridRetriever(papers)

        return retriever.retrieve_top_papers_with_scores(query, k)
