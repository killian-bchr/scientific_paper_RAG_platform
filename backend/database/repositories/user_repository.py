from typing import List, Optional

from sqlalchemy.orm import Session

from backend.database.tables import UserORM


class UserRepository:
    @staticmethod
    def fetch_user_by_username(
        session: Session,
        username: str,
    ) -> Optional[UserORM]:
        return session.query(UserORM).filter_by(username=username).first()

    @staticmethod
    def fetch_user_by_id(session: Session, user_id: int) -> UserORM:
        return session.query(UserORM).filter(UserORM.id == user_id).first()

    @staticmethod
    def fetch_all_users(session: Session) -> List[UserORM]:
        return session.query(UserORM).all()

    @staticmethod
    def delete_user(session: Session, user: UserORM) -> None:
        return session.delete(user)
