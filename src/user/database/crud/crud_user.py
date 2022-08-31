from typing import List
from sqlalchemy.orm import Session

from user.database.models.User import User
from user.database.crud.crud_base import CRUDBase

class CRUDUser(CRUDBase):
    def __init__(self, connection: Session):
        super().__init__(connection, User)

    def create(self, *, obj_in: User) -> User:
        self._connection.add(obj_in)
        self._connection.commit()
        self._connection.refresh(obj_in)
        return obj_in

    def get_users(self, criteria) -> List[User]:
        return super().get()