from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user.database import deps
from user.managers.user_manager import UserManager
from user.schemas.UserResponse import UserResponse
from user.v1.endpoints.create_user.schemas.CreateUserRequest import CreateUserRequest
from user.v1.endpoints.mappers.user_mapper import UserMapper

router = APIRouter()


@router.post(
    "/users",
    response_description="User details",
    response_model=UserResponse,
    tags=["user"])
def create_user(
        *,
        db_connection: Session = Depends(deps.get_db),
        user: CreateUserRequest) -> UserResponse:
    """_summary_

    Args:
        user (CreateUserRequest): _description_
        db_connection (Session, optional): _description_. Defaults to Depends(deps.get_db).

    Returns:
        UserResponse: _description_
    """
    domain_request = UserMapper.to_domain(user)
    user_manager = UserManager(db_connection)
    domain_response = user_manager.create_user(domain_request)

    api_response = UserMapper.to_api(domain_response)
    return api_response
