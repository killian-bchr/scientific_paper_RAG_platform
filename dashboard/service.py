from datetime import date
from typing import List, Tuple

from constants import DefaultValues
from utils import Utils

from database.tables import CategoryORM, ChunkORM, DomainORM, PaperORM
from retriever import HybridRetriever


class Service:
    @staticmethod
    def filter_chunks_by_type(
        chunks: List[ChunkORM],
        chunk_type: str,
    ) -> List[ChunkORM]:
        if chunk_type == DefaultValues.ALL:
            return chunks
        return [c for c in chunks if c.chunk_type == chunk_type]

    @staticmethod
    def compute_start_and_end_date(start_year: int, end_year: int) -> Tuple[date, date]:
        start_date, end_date = None, None

        if start_year != DefaultValues.ALL:
            start_date = date(start_year, 1, 1)

        if end_year != DefaultValues.ALL:
            end_date = date(end_year, 12, 31)

        if start_date and end_date and start_date > end_date:
            raise ValueError("Start year must be before end year")

        return start_date, end_date

    @staticmethod
    def paper_matches_category(paper: PaperORM, category: CategoryORM) -> bool:
        if category == DefaultValues.ALL:
            return True

        if category in [c.name for c in paper.categories]:
            return True

        return False

    @staticmethod
    def paper_matches_domain(paper: PaperORM, domain: DomainORM) -> bool:
        if domain == DefaultValues.ALL:
            return True

        if domain in [d.name for d in paper.domains]:
            return True

        return False

    @staticmethod
    def is_paper_matches_filters(
        paper: PaperORM,
        domain: DomainORM,
        category: CategoryORM,
    ) -> bool:
        is_matching_category = Service.paper_matches_category(paper, category)
        is_matching_domain = Service.paper_matches_domain(paper, domain)

        return is_matching_category & is_matching_domain

    @staticmethod
    def filter_papers(
        papers: List[PaperORM],
        domain: DomainORM,
        category: CategoryORM,
    ) -> List[PaperORM]:
        return [
            p for p in papers if Service.is_paper_matches_filters(p, domain, category)
        ]

    @staticmethod
    def fetch_paper_selected(papers: List[PaperORM], paper_title: str) -> PaperORM:
        paper_titles = Utils.create_papers_dict(papers)
        return paper_titles[paper_title]

    @staticmethod
    def retrieve_top_k_papers(
        papers: List[PaperORM],
        query: str,
        k: int = 10,
    ) -> List[int]:
        retriever = HybridRetriever(papers)

        return retriever.top_k_papers(query, k)
