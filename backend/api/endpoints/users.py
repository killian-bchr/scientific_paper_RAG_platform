from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.api.dependencies import get_admin_user, get_db
from backend.schemas.user import User
from backend.services import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[User])
async def get_users(
    session: Session = Depends(get_db),
    admin_user=Depends(get_admin_user),
):
    users = UserService.get_all_users(session)
    if not users:
        return []

    return users


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    session: Session = Depends(get_db),
    admin_user=Depends(get_admin_user),
):
    user = UserService.get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    session: Session = Depends(get_db),
    admin_user=Depends(get_admin_user),
):
    UserService.delete_user_by_id(session, user_id)
