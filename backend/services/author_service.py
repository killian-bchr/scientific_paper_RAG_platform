from typing import List

from helpers.utils import Utils
from sqlalchemy.orm import Session

from backend.database.tables import AuthorORM


class AuthorService:
    @staticmethod
    def get_all_authors(session: Session) -> List[AuthorORM]:
        return Utils.fetch_all_authors(session)

    @staticmethod
    def get_author_by_id(session: Session, author_id: int) -> AuthorORM:
        return session.query(AuthorORM).filter(AuthorORM.id == author_id).first()

    @staticmethod
    def create_author() -> AuthorORM:
        # TODO
        pass
