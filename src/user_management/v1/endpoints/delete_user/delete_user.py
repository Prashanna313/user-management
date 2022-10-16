
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user_management.database import deps
from user_management.managers.user_manager import UserManager

router = APIRouter()


@router.delete(
    "/users/{user_id}",
    description="Delete an user by id",
    status_code=204,
    tags=["user"])
def delete_user(
        user_id: str,
        db_connection: Session = Depends(deps.get_db)) -> None:
    """
    Delete a specific user by id.

    Args:
        user_id (str): Unique ID of the user
        db_connection (Session, optional): _description_. Defaults to Depends(deps.get_db).
    """
    user_manager = UserManager(db_connection)
    user_manager.delete_user(id_=user_id)

    return
