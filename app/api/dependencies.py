import jose as jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.services import AuthService
from database.session import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    with get_session(commit=True) as session:
        yield session


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = AuthService.decode_token(token)
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
    if current_user["role"] != "admin":
        raise HTTPException(403, "Admin only")
    return current_user
