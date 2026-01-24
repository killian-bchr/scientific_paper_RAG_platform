from typing import List

from helpers.utils import Utils
from sqlalchemy.orm import Session

from backend.database.tables import ChunkORM, PaperORM


class PaperService:
    @staticmethod
    def get_all_papers(session: Session) -> List[PaperORM]:
        return Utils.fetch_all_papers(session)

    @staticmethod
    def get_paper_by_id(session: Session, paper_id: int) -> PaperORM:
        return Utils.fetch_paper_by_id(session, paper_id)

    @staticmethod
    def get_chunks_by_paper_id(session: Session, paper_id: int) -> List[ChunkORM]:
        return Utils.fetch_chunks_by_paper_id(session, paper_id)
