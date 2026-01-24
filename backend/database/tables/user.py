from datetime import datetime

from sqlalchemy import Column, Date, Integer, String

from backend.core.constants import UserRole
from backend.database.base import Base


class UserORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default=UserRole.USER.value)
    created_at = Column(Date, default=datetime.utcnow)
