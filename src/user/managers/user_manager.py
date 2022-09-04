from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from user.database.crud.crud_user import CRUDUser
from user.database.models.User import User
from user.v1.endpoints.get_user.schemas.GetUserCriteria import GetUserCriteria


class UserManager:
    def __init__(self, connection: Session) -> None:
        self._crud_user: CRUDUser = CRUDUser(connection)

    def create_user(self, user: User) -> User:
        return self._crud_user.create_user(user=user)

    def delete_user(self, id_: UUID) -> None:
        return self._crud_user.delete_user(id_=id_)

    def get_users(self, criteria: GetUserCriteria) -> List[User]:
        return self._crud_user.get_users(criteria)

    def update_user(self, id_: UUID, user: User) -> User:
        return self._crud_user.update(id_=id_, obj_in=user)