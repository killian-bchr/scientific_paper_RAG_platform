from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.database.tables.association_tables import paper_domain


class DomainORM(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False, index=True)

    papers = relationship(
        "PaperORM",
        secondary=paper_domain,
        back_populates="domains",
    )

    categories = relationship(
        "CategoryORM", back_populates="domain", cascade="all, delete-orphan"
    )
