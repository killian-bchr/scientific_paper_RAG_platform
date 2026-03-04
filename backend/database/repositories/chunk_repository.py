from typing import List

from sqlalchemy.orm import Session

from backend.database.tables import ChunkORM


class ChunkRepository:
    @staticmethod
    def fetch_all_chunks(session: Session) -> List[ChunkORM]:
        return session.query(ChunkORM).all()

    @staticmethod
    def fetch_chunk_by_id(session: Session, chunk_id: int) -> ChunkORM:
        return session.query(ChunkORM).filter(ChunkORM.id == chunk_id).first()

    @staticmethod
    def fetch_chunks_by_type(session: Session, chunk_type: str) -> List[ChunkORM]:
        return session.query(ChunkORM).filter(ChunkORM.chunk_type == chunk_type).all()

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

    @staticmethod
    def delete_chunk(session: Session, chunk: ChunkORM) -> None:
        session.delete(chunk)

    @staticmethod
    def delete_chunk_by_id(session: Session, chunk_id: int) -> None:
        chunk = ChunkRepository.fetch_chunk_by_id(session, chunk_id)
        if not chunk:
            raise ValueError(f"Chunk : {chunk_id} not found.")

        ChunkRepository.delete_chunk(session, chunk)

    @staticmethod
    def delete_chunks_by_type(session: Session, chunk_type: str) -> None:
        chunks = ChunkRepository.fetch_chunks_by_type(session, chunk_type)
        if not chunks:
            return

        for c in chunks:
            ChunkRepository.delete_chunk(session, c)

    @staticmethod
    def get_window_chunks(
        session: Session, center_chunk_id: int, window=2
    ) -> List[ChunkORM]:
        result = []
        visited = set()

        def traverse_left(chunk_id, n):
            if n == 0 or chunk_id is None or chunk_id in visited:
                return
            visited.add(chunk_id)
            chunk = chunk_dict[chunk_id]
            result.append(chunk)
            traverse_left(chunk.left_chunk_id, n - 1)

        def traverse_right(chunk_id, n):
            if n == 0 or chunk_id is None or chunk_id in visited:
                return
            visited.add(chunk_id)
            chunk = chunk_dict[chunk_id]
            result.append(chunk)
            traverse_right(chunk.right_chunk_id, n - 1)

        center_chunk = chunk_dict[center_chunk_id]
        result.append(center_chunk)
        visited.add(center_chunk_id)

        traverse_left(center_chunk.left_chunk_id, window)
        traverse_right(center_chunk.right_chunk_id, window)

        result.sort(key=lambda c: (c.page_no, c.left_chunk_id or -1))

        return result
