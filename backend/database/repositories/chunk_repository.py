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
        session: Session,
        center_chunk_id: int,
        window: int = 2,
    ) -> List[ChunkORM]:

        result = []
        visited = set()

        center_chunk = ChunkRepository.fetch_chunk_by_id(session, center_chunk_id)
        if center_chunk is None:
            return []

        result.append(center_chunk)
        visited.add(center_chunk.id)

        # LEFT
        current = center_chunk
        for _ in range(window):
            if current.previous_chunk_id is None:
                break

            prev_chunk = ChunkRepository.fetch_chunk_by_id(
                session,
                current.previous_chunk_id,
            )
            if prev_chunk is None or prev_chunk.id in visited:
                break

            result.append(prev_chunk)
            visited.add(prev_chunk.id)
            current = prev_chunk

        # RIGHT
        current = center_chunk
        for _ in range(window):
            if current.next_chunk_id is None:
                break

            next_chunk = ChunkRepository.fetch_chunk_by_id(
                session,
                current.next_chunk_id,
            )
            if next_chunk is None or next_chunk.id in visited:
                break

            result.append(next_chunk)
            visited.add(next_chunk.id)
            current = next_chunk

        result.sort(key=lambda c: c.id)

        return result
