from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.database.tables.association_tables import paper_category


class CategoryORM(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    domain_id = Column(Integer, ForeignKey("domains.id"), nullable=False)

    domain = relationship("DomainORM", back_populates="categories")
    papers = relationship(
        "PaperORM",
        secondary=paper_category,
        back_populates="categories",
    )
