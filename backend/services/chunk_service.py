from typing import List

from sqlalchemy.orm import Session

from database.tables import ChunkORM
from helpers.utils import Utils


class ChunkService:
    @staticmethod
    def get_all_chunks(session: Session) -> List[ChunkORM]:
        return Utils.fetch_all_chunks(session)

    @staticmethod
    def get_chunk_by_id(session: Session, chunk_id: int) -> ChunkORM:
        return session.query(ChunkORM).filter(ChunkORM.id == chunk_id).first()
