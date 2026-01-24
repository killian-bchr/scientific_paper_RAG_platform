from typing import List

from sqlalchemy.orm import Session

from backend.database.tables import ChunkORM


class ChunkRepository:
    @staticmethod
    def fetch_all_chunks(session: Session) -> List[ChunkORM]:
        return session.query(ChunkORM).all()

    @staticmethod
    def fetch_chunks_by_paper_id(session: Session, paper_id: int) -> List[ChunkORM]:
        return (
            session.query(ChunkORM)
            .filter(ChunkORM.paper_id == paper_id)
            .order_by(ChunkORM.page_no, ChunkORM.id)
            .all()
        )

    @staticmethod
    def count_chunks(session: Session) -> int:
        return session.query(ChunkORM).count()
