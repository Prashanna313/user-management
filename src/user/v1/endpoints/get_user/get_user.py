from typing import Any, List
from app import crud, models, schemas
from app.api import deps
from user.core.config import settings
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from user_management_client_v1.models.get_users_response import GetUsersResponse
from user_management_client_v1.models.user import User
from user.database.Session import SessionLocal

router = APIRouter()


@router.get("/", response_model=GetUsersResponse)
def read_users(
    db: Session = Depends(SessionLocal()),
    skip: int = 0,
    limit: int = 100,) -> GetUsersResponse:
    """_summary_

    Args:
        db (Session, optional): _description_. Defaults to Depends(SessionLocal()).
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        GetUsersResponse: _description_
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user
