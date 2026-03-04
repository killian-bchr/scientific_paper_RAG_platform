from typing import List

from sqlalchemy.orm import Session

from backend.database.repositories import ChunkRepository
from backend.database.tables import ChunkORM


class ChunkService:
    @staticmethod
    def get_all_chunks(session: Session) -> List[ChunkORM]:
        return ChunkRepository.fetch_all_chunks(session)

    @staticmethod
    def get_chunk_by_id(session: Session, chunk_id: int) -> ChunkORM:
        return ChunkRepository.fetch_chunk_by_id(session, chunk_id)

    @staticmethod
    def delete_chunk_by_id(session: Session, chunk_id: int) -> None:
        return ChunkRepository.delete_chunk_by_id(session, chunk_id)

    @staticmethod
    def delete_chunks_by_type(session: Session, chunk_type: str) -> None:
        return ChunkRepository.delete_chunks_by_type(session, chunk_type)
