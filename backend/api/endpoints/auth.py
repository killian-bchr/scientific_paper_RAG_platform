from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from backend.api.dependencies import get_db
from backend.core.exceptions import InvalidPasswordError, UserNotFoundError
from backend.schemas.auth import CreateUserRequest, TokenResponse
from backend.services import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    create_user_request: CreateUserRequest,
    session: Session = Depends(get_db),
):
    try:
        AuthService.create_user(
            session,
            create_user_request.username,
            create_user_request.password,
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_db),
):
    try:
        user = AuthService.authenticate(session, form_data.username, form_data.password)

    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User '{form_data.username}' not found",
        )

    except InvalidPasswordError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Authentication service error: {str(e)}",
        )

    token = AuthService.create_access_token(user.id, user.username, user.role)
    return {"access_token": token}
