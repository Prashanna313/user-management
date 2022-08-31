
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user.database import deps
from user.managers.user_manager import UserManager

router = APIRouter()


@router.delete(
    "/users/{user_id}",
    description="Delete an user by id",
    status_code=204,
    tags=["user"])
def delete_user(
        user_id: str,
        db_connection: Session = Depends(deps.get_db)):
    """
    Delete a specific user by id.
    """
    user_manager = UserManager(db_connection)
    user_manager.delete_user(id_=user_id)

    return
