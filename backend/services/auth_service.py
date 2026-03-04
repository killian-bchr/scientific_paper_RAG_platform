from datetime import datetime, timedelta
from typing import Dict

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from backend.core.config import Config
from backend.core.exceptions import InvalidPasswordError, UserNotFoundError
from backend.database.repositories import UserRepository
from backend.database.tables.user import UserORM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    def authenticate(session: Session, username: str, password: str) -> UserORM:
        user = UserRepository.fetch_user_by_username(session, username)
        if not user:
            raise UserNotFoundError(f"User '{username}' not found")

        if not pwd_context.verify(password, user.hashed_password):
            raise InvalidPasswordError("Invalid password")

        return user

    @staticmethod
    def create_access_token(user_id: int, username: str, role: str) -> Dict:
        exp_minutes = Config.ACCESS_TOKEN_EXPIRE_MINUTES
        token_exp = datetime.utcnow() + timedelta(minutes=exp_minutes)
        payload = {
            "sub": username,
            "id": user_id,
            "role": role,
            "exp": token_exp,
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm=Config.ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> Dict:
        return jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
