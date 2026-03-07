from dataclasses import dataclass
from typing import List, Optional

from backend.database.tables import PaperORM
from backend.models.chunks_ranked import ChunkRanked


@dataclass(eq=True)
class PaperRanked:
    paper: PaperORM
    score: float
    chunks: Optional[List[ChunkRanked]] = None
