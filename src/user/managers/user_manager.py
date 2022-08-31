from datetime import datetime
from typing import List
from uuid import uuid4
from sqlalchemy.orm import Session
# from user_management_client_v1.models.user import User as ApiUser
from user.database.crud.crud_user import CRUDUser
from user.database.models.Gender import Gender
from user.database.models.User import User
from user.database.models.UserStatus import UserStatus


class UserManager:
    def __init__(self, connection: Session) -> None:
        self._crud_user: CRUDUser = CRUDUser(connection)

    # def create_user(self, user: ApiUser = None):
    #     domain_user = User(
    #         created_by="system",
    #         created_on=datetime.now(),
    #         id=uuid4(),
    #         modified_by="system",
    #         modified_on=datetime.now(),
    #         date_of_birth=datetime.now().date(),
    #         gender=Gender.MALE,
    #         email="foo@bar.com",
    #         first_name="foo",
    #         hashed_password="1234",
    #         last_name="bar",
    #         row_version=str(uuid4()),
    #         status=UserStatus.ACTIVE)
    #     return self._crud_user.create(obj_in=domain_user)

    def get_users(self, criteria=None) -> List[User]:
        return self._crud_user.get_users(criteria)
