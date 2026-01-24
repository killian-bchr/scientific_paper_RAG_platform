from typing import List

from helpers.utils import Utils
from sqlalchemy.orm import Session

from backend.database.tables import CategoryORM


class CategoryService:
    @staticmethod
    def get_all_categories(session: Session) -> List[CategoryORM]:
        return Utils.fetch_all_categories(session)

    @staticmethod
    def get_category_by_id(session: Session, category_id: int) -> CategoryORM:
        return session.query(CategoryORM).filter(CategoryORM.id == category_id).first()

    @staticmethod
    def create_category() -> CategoryORM:
        # TODO
        pass
