from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from user.database import deps
from user.managers.user_manager import UserManager
from user.schemas.UserResponse import UserResponse
from user.v1.endpoints.get_user.schemas.GetUserCriteria import GetUserCriteria
from user.v1.endpoints.get_user.schemas.GetUserResponse import GetUserResponse
from user.v1.endpoints.mappers.user_mapper import UserMapper

router = APIRouter()


@router.get(
    "/users",
    response_description="List of Users",
    response_model=GetUserResponse,
    tags=["user"])
def read_users(
        db_connection: Session = Depends(deps.get_db),
        email: Optional[EmailStr] = None,
        limit: int = 100,
        skip: int = 0,
        user_ids: Optional[List[str]] = Query(None)) -> GetUserResponse:
    """
    Get all users

    Args:
        db_connection (Session, optional): _description_. Defaults to Depends(deps.get_db).
        email (Optional[EmailStr], optional): _description_. Defaults to None.
        limit (int, optional): _description_. Defaults to 100.
        skip (int, optional): _description_. Defaults to 0.
        user_ids (Optional[List[str]], optional): Unique IDs of the users. Defaults to Query(None).

    Returns:
        GetUserResponse: _description_
    """

    api_criteria = GetUserCriteria(
        email=email,
        limit=limit,
        skip=skip,
        user_ids=user_ids)

    user_manager = UserManager(db_connection)
    domain_response = user_manager.get_users(api_criteria)

    api_response = list(map(UserMapper.to_api, domain_response))
    return GetUserResponse(users=api_response)


@router.get(
    "/users/{user_id}",
    response_description="User details",
    response_model=UserResponse,
    tags=["user"])
def read_user_by_id(
        user_id: str,
        db_connection: Session = Depends(deps.get_db)) -> UserResponse:
    """
    Get a specific user by id.

    Args:
        user_id (str): Unique ID of the user
        db_connection (Session, optional): db connection. Defaults to Depends(deps.get_db).

    Raises:
        HTTPException: _description_

    Returns:
        UserResponse: _description_
    """
    api_criteria = GetUserCriteria(user_ids=[user_id])

    user_manager = UserManager(db_connection)
    domain_response = user_manager.get_users(api_criteria)

    if not domain_response:
        raise HTTPException(status_code=404, detail="User not found")

    api_response = UserMapper.to_api(domain_response[0])
    return api_response
