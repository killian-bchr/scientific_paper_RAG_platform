import jose as jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.core.constants import UserRole
from backend.database.repositories import UserRepository
from backend.database.session import get_session
from backend.services import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_db():
    with get_session(commit=True) as session:
        yield session


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_db),
):
    try:
        payload = AuthService.decode_token(token)
        username = payload.get("sub")
        user = UserRepository.fetch_user_by_username(session, username)
        if not user:
            raise HTTPException(status_code=401, detail=f"User {username} not found")

        return {
            "username": payload["sub"],
            "id": payload["id"],
            "role": payload["role"],
        }

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")


def get_admin_user(current_user=Depends(get_current_user)):
    if current_user["role"] != UserRole.ADMIN.value:
        raise HTTPException(403, "Admin only")
    return current_user
