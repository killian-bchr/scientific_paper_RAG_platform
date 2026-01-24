from typing import List

from sqlalchemy.orm import Session

from backend.database.repositories import ChunkRepository, PaperRepository
from backend.database.tables import ChunkORM, PaperORM


class PaperService:
    @staticmethod
    def get_all_papers(session: Session) -> List[PaperORM]:
        return PaperRepository.fetch_all_papers(session)

    @staticmethod
    def get_paper_by_id(session: Session, paper_id: int) -> PaperORM:
        return PaperRepository.fetch_paper_by_id(session, paper_id)

    @staticmethod
    def get_chunks_by_paper_id(session: Session, paper_id: int) -> List[ChunkORM]:
        return ChunkRepository.fetch_chunks_by_paper_id(session, paper_id)
