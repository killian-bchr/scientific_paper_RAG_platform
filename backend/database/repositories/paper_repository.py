from datetime import date, datetime
from typing import List, Optional, Union

from sqlalchemy.orm import Query, Session, joinedload

from backend.core.date_utils import DateUtils
from backend.database.tables import CategoryORM, DomainORM, PaperORM


class PaperRepository:
    @staticmethod
    def papers_base_query(session: Session) -> Query[PaperORM]:
        return session.query(PaperORM).options(
            joinedload(PaperORM.domains),
            joinedload(PaperORM.categories),
            joinedload(PaperORM.authors),
        )

    @staticmethod
    def fetch_all_papers(session: Session) -> List[PaperORM]:
        base_query = PaperRepository.papers_base_query(session)
        return base_query.all()

    @staticmethod
    def fetch_paper_by_id(session: Session, paper_id: int) -> PaperORM:
        base_query = PaperRepository.papers_base_query(session)
        return base_query.filter(PaperORM.id == paper_id).first()

    @staticmethod
    def fetch_papers_by_ids(
        session: Session, paper_ids: Optional[List[int]]
    ) -> List[PaperORM]:
        base_query = PaperRepository.papers_base_query(session)

        if paper_ids is None or len(paper_ids) == 0:
            return base_query.all()

        return base_query.filter(PaperORM.id.in_(paper_ids)).all()

    @staticmethod
    def fetch_paper_by_title(session: Session, title: str) -> PaperORM:
        base_query = PaperRepository.papers_base_query(session)
        return base_query.filter(PaperORM.title == title).one()

    @staticmethod
    def fetch_papers_by_period(
        session: Session,
        start_date: Optional[Union[datetime, date, str]] = None,
        end_date: Optional[Union[datetime, date, str]] = None,
    ) -> List[PaperORM]:
        start_date = DateUtils.parse_date(start_date)
        end_date = DateUtils.parse_date(end_date)

        query = PaperRepository.papers_base_query(session)

        if start_date:
            query = query.filter(PaperORM.publication_date >= start_date)

        if end_date:
            query = query.filter(PaperORM.publication_date <= end_date)

        return query.all()

    @staticmethod
    def fetch_filtered_papers(
        session: Session,
        domain_id: Optional[int] = None,
        category_id: Optional[int] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> List[PaperORM]:
        start_date = DateUtils.parse_date(start_date)
        end_date = DateUtils.parse_date(end_date)

        query = PaperRepository.papers_base_query(session)

        if domain_id:
            query = query.join(PaperORM.domains).filter(DomainORM.id == domain_id)

        if category_id:
            query = query.join(PaperORM.categories).filter(
                CategoryORM.id == category_id
            )

        if start_date:
            query = query.filter(PaperORM.publication_date >= start_date)

        if end_date:
            query = query.filter(PaperORM.publication_date <= end_date)

        query = query.distinct()

        return query.all()

    @staticmethod
    def get_existing_paper(session: Session, paper_id: str) -> Optional[PaperORM]:
        return session.query(PaperORM).filter_by(arxiv_id=paper_id).first()

    @staticmethod
    def count_papers(session: Session) -> int:
        return session.query(PaperORM).count()

    @staticmethod
    def delete_paper(session: Session, paper: PaperORM) -> None:
        session.delete(paper)

    @staticmethod
    def delete_paper_by_id(session: Session, paper_id: int) -> None:
        paper = PaperRepository.fetch_paper_by_id(session, paper_id)
        if not paper:
            raise ValueError(f"Paper : {paper_id} not found.")
        PaperRepository.delete_paper(session, paper)
