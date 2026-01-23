from typing import List

from sqlalchemy.orm import Session

from database.tables import AuthorORM
from helpers.utils import Utils


class AuthorService:
    @staticmethod
    def get_all_authors(session: Session) -> List[AuthorORM]:
        return Utils.fetch_all_authors(session)

    @staticmethod
    def get_author_by_id(session: Session, author_id: int) -> AuthorORM:
        return session.query(AuthorORM).filter(AuthorORM.id == author_id).first()

    @staticmethod
    def create_author() -> AuthorORM:
        pass
