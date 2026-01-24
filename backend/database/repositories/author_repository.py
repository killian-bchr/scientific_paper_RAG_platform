from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from backend.database.tables import AuthorORM


class AuthorRepository:
    @staticmethod
    def fetch_all_authors(session: Session) -> List[AuthorORM]:
        return (
            session.query(AuthorORM)
            .options(
                joinedload(AuthorORM.papers),
            )
            .all()
        )

    @staticmethod
    def get_existing_author(session: Session, name: str) -> Optional[AuthorORM]:
        return session.query(AuthorORM).filter_by(name=name).first()

    @staticmethod
    def count_authors(session: Session) -> int:
        return session.query(AuthorORM).count()
