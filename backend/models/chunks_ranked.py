from dataclasses import dataclass

from backend.database.tables import ChunkORM


@dataclass(eq=True)
class ChunkRanked:
    chunk: ChunkORM
    score: float
