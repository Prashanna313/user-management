from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from user.database import deps
from user.managers.user_manager import UserManager
from user.schemas.UserResponse import UserResponse
from user.v1.endpoints.get_user.schemas.GetUserCriteria import GetUserCriteria
from user.v1.endpoints.mappers.user_mapper import UserMapper
from user.v1.endpoints.update_user.schemas.UpdateUserRequest import UpdateUserRequest

router = APIRouter()

@router.patch(
    "/users/{user_id}",
    response_description="User details",
    response_model=UserResponse,
    tags=["user"])
def update_user(
        user: UpdateUserRequest,
        user_id: str,
        db_connection: Session = Depends(deps.get_db)) -> UserResponse:
    """
    Update a specific user by id.

    Args:
        user_id (str): Unique ID of the user
        db_connection (Session, optional): db connection. Defaults to Depends(deps.get_db).

    Raises:
        HTTPException: 404 - User not found

    Returns:
        UserResponse: _description_
    """
    domain_request = GetUserCriteria(user_ids=[user_id])

    user_manager = UserManager(db_connection)
    domain_response = user_manager.update_user(id_=user_id, user=domain_request)

    api_response = UserMapper.to_api(domain_response)
    return api_response
