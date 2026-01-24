from typing import List

from sqlalchemy.orm import Session

from backend.database.repositories import CategoryRepository
from backend.database.tables import CategoryORM


class CategoryService:
    @staticmethod
    def get_all_categories(session: Session) -> List[CategoryORM]:
        return CategoryRepository.fetch_all_categories(session)

    @staticmethod
    def get_category_by_id(session: Session, category_id: int) -> CategoryORM:
        return session.query(CategoryORM).filter(CategoryORM.id == category_id).first()

    @staticmethod
    def create_category() -> CategoryORM:
        # TODO
        pass
