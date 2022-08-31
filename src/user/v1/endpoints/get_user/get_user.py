from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
# from user.database.models.User import User
from user.managers.user_manager import UserManager
from user.schemas.UserBase import UserBase
from user.v1 import deps
from user.v1.endpoints.get_user.mappers.user_mapper import UserMapper
from user.v1.endpoints.get_user.schemas.GetUserCriteria import GetUserCriteria
from user.v1.endpoints.get_user.schemas.GetUserResponse import GetUserResponse

router = APIRouter()
# @router.post("/users")
# def create_user(
#         *,
#         db_connection: Session = Depends(deps.get_db),
#         user: UserBase) -> Any:
#     user_manager = UserManager(db_connection)
#     users = user_manager.create_user(user)
#     return users


@router.get(
    "/users",
    response_description="List of Users",
    response_model=GetUserResponse)
def read_users(
        db_connection: Session = Depends(deps.get_db),
        email: Optional[EmailStr] = None,
        limit: int = 100,
        skip: int = 0,
        user_ids: Optional[List[str]] = Query(None)) -> GetUserResponse:

    api_criteria = GetUserCriteria(
        email=email,
        limit=limit,
        skip=skip,
        user_ids=user_ids)

    user_manager = UserManager(db_connection)
    domain_users = user_manager.get_users(api_criteria)

    api_users = list(map(UserMapper.to_api, domain_users))
    return GetUserResponse(users=api_users)


@router.get(
    "/users/{user_id}",
    response_description="User details",
    response_model=UserBase)
def read_user_by_id(
        user_id: str,
        db_connection: Session = Depends(deps.get_db)) -> UserBase:
    """
    Get a specific user by id.
    """
    api_criteria = GetUserCriteria(user_ids=[user_id])

    user_manager = UserManager(db_connection)
    domain_user = user_manager.get_users(api_criteria)

    api_user = UserMapper.to_api(domain_user[0])
    return api_user
