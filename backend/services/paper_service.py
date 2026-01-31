from datetime import date
from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from backend.database.repositories import ChunkRepository, PaperRepository
from backend.database.tables import ChunkORM, PaperORM


class PaperService:
    @staticmethod
    def compute_start_and_end_date(
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
    ) -> Tuple[date, date]:
        start_date, end_date = None, None

        if start_year:
            start_date = date(start_year, 1, 1)

        if end_year:
            end_date = date(end_year, 12, 31)

        if start_date and end_date and start_date > end_date:
            raise ValueError("Start year must be before end year")

        return start_date, end_date

    @staticmethod
    def get_filtered_papers(
        session: Session,
        domain_id: Optional[int] = None,
        category_id: Optional[int] = None,
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
    ):
        start_date, end_date = PaperService.compute_start_and_end_date(
            start_year, end_year
        )
        return PaperRepository.fetch_filtered_papers(
            session=session,
            domain_id=domain_id,
            category_id=category_id,
            start_date=start_date,
            end_date=end_date,
        )

    @staticmethod
    def get_all_papers(session: Session) -> List[PaperORM]:
        return PaperRepository.fetch_all_papers(session)

    @staticmethod
    def get_paper_by_id(session: Session, paper_id: int) -> PaperORM:
        return PaperRepository.fetch_paper_by_id(session, paper_id)

    @staticmethod
    def get_chunks_by_paper_id(session: Session, paper_id: int) -> List[ChunkORM]:
        return ChunkRepository.fetch_chunks_by_paper_id(session, paper_id)

    @staticmethod
    def delete_paper_by_id(session: Session, paper_id: int) -> None:
        return PaperRepository.delete_paper_by_id(session, paper_id)
