from typing import List, Optional

from sqlalchemy.orm import Session

from backend.core.date_utils import DateUtils
from backend.database.repositories import ChunkRepository, PaperRepository
from backend.database.tables import ChunkORM, PaperORM


class PaperService:
    @staticmethod
    def get_filtered_papers(
        session: Session,
        domain_id: Optional[int] = None,
        category_id: Optional[int] = None,
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
    ):
        start_date, end_date = DateUtils.compute_start_and_end_date(
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
