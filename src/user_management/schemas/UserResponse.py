from datetime import datetime
from uuid import UUID
from user_management.schemas.UserBase import UserBase


class UserResponse(UserBase):
    createdBy: str
    createdOn: datetime
    id: UUID
    modifiedBy: str
    modifiedOn: datetime
