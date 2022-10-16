from datetime import date
from typing import Optional
from pydantic import BaseModel
from user_management.schemas.Address import Address
from user_management.schemas.Gender import Gender
from user_management.schemas.UserBase import UserBase
from user_management.schemas.UserStatus import UserStatus


class UpdateUserRequest(BaseModel):
    address: Optional[Address] = None
    dateOfBirth: date
    firstName: str
    gender: Gender
    lastName: str
    status: UserStatus
