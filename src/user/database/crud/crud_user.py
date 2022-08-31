from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from user.database.crud.crud_base import CRUDBase
from user.database.models.User import User
from user.database.models.UserSpecifications import UserSpecifications
from user.v1.endpoints.get_user.schemas.GetUserCriteria import GetUserCriteria


class CRUDUser(CRUDBase):
    def __init__(self, connection: Session):
        super().__init__(connection, User)

    def create_user(self, *, user: User) -> User:
        return super().create(obj_in=user)

    def delete_user(self, *, id_: UUID) -> None:
        return super().delete(id_=id_)

    def get_users(self, criteria: GetUserCriteria) -> List[User]:
        where_clause = UserSpecifications.create_where(criteria)
        return super().get(
            limit=criteria.limit,
            skip=criteria.skip,
            where_clause=where_clause)
