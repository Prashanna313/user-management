from typing import List
from sqlalchemy.orm import Session
from user.database.crud.crud_user import CRUDUser
from user.database.models.User import User

class UserManager:
    def __init__(self, connection: Session) -> None:
        self._crud_user: CRUDUser = CRUDUser(connection)

    def get_users(self, criteria = None) -> List[User]:
        return self._crud_user.get()
