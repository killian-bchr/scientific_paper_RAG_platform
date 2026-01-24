from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.database.tables.association_tables import paper_author


class AuthorORM(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)

    papers = relationship(
        "PaperORM",
        secondary=paper_author,
        back_populates="authors",
    )
