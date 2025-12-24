from sqlalchemy import Column, Date, Integer, String, Text
from sqlalchemy.orm import relationship

from database.base import Base
from database.tables.association_tables import paper_author, paper_domain, paper_category


class PaperORM(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    arxiv_id = Column(String, unique=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    pdf_url = Column(String)
    abstract = Column(Text)
    publication_date = Column(Date)

    authors = relationship(
        "AuthorORM",
        secondary=paper_author,
        back_populates="papers",
    )

    domains = relationship(
        "DomainORM",
        secondary=paper_domain,
        back_populates="papers",
    )
    
    categories = relationship(
        "CategoryORM",
        secondary=paper_category,
        back_populates="papers",
    )

    chunks = relationship(
        "ChunkORM",
        back_populates="paper",
        cascade="all, delete-orphan"
    )
