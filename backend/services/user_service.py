from typing import List

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from backend.core.constants import UserRole
from backend.database.crud import CRUD
from backend.database.repositories import UserRepository
from backend.database.tables.user import UserORM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    @staticmethod
    def create_user(session: Session, username: str, password: str) -> UserORM:
        existing = UserRepository.fetch_user_by_username(session, username)
        if existing:
            raise ValueError(f"Username '{username}' is already taken")

        hashed_password = pwd_context.hash(password)
        user = CRUD.user_to_orm(
            session,
            username,
            hashed_password,
        )

        return user

    @staticmethod
    def get_all_users(session: Session) -> List[UserORM]:
        return UserRepository.fetch_all_users(session)

    @staticmethod
    def get_user_by_id(session: Session, user_id: int) -> UserORM:
        return UserRepository.fetch_user_by_id(session, user_id)

    @staticmethod
    def delete_user_by_id(session: Session, user_id: int) -> None:
        user = UserRepository.fetch_user_by_id(session, user_id)
        if user.role == UserRole.ADMIN.value:
            raise ValueError(f"Impossible to delete admin user {user_id}.")

        UserRepository.delete_user(session, user)
