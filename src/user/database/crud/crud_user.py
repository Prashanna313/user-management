from typing import List
from sqlalchemy.orm import Session

from user.database.models.User import User
from user.database.crud.crud_base import CRUDBase

class CRUDUser(CRUDBase):
    def __init__(self, connection: Session):
        super().__init__(connection, User)

    def create(self, db: Session, *, obj_in: User) -> User:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def get_users(self, criteria) -> List[User]:
        return super().get()