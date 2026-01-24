from typing import List

from helpers.utils import Utils
from sqlalchemy.orm import Session

from backend.database.tables import ChunkORM


class ChunkService:
    @staticmethod
    def get_all_chunks(session: Session) -> List[ChunkORM]:
        return Utils.fetch_all_chunks(session)

    @staticmethod
    def get_chunk_by_id(session: Session, chunk_id: int) -> ChunkORM:
        return session.query(ChunkORM).filter(ChunkORM.id == chunk_id).first()
