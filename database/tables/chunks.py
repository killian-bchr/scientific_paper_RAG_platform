from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database.base import Base


class ChunkORM(Base):
    __tablename__ = "chunks"

    id = Column(Integer, autoincrement=True, primary_key=True)
    paper_id = Column(
        Integer, ForeignKey("papers.id", ondelete="CASCADE"), index=True, nullable=False
    )
    chunk_type = Column(String)
    page_no = Column(Integer)
    content = Column(Text)
    embedding = Column(Vector(384))

    paper = relationship("PaperORM", back_populates="chunks")
