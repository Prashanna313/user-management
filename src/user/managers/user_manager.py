from datetime import datetime
from typing import List
from uuid import uuid4
from sqlalchemy.orm import Session
from user.database.crud.crud_user import CRUDUser
from user.database.models.User import User


class UserManager:
    def __init__(self, connection: Session) -> None:
        self._crud_user: CRUDUser = CRUDUser(connection)

    def create_user(self, user: User) -> User:
        return self._crud_user.create(obj_in=user)

    def get_users(self, criteria) -> List[User]:
        return self._crud_user.get_users(criteria)
