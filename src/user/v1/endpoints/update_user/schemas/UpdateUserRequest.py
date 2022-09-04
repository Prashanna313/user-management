from datetime import date
from typing import Optional
from pydantic import BaseModel
from user.schemas.Address import Address
from user.schemas.Gender import Gender
from user.schemas.UserBase import UserBase
from user.schemas.UserStatus import UserStatus


class UpdateUserRequest(BaseModel):
    address: Optional[Address] = None
    dateOfBirth: date
    firstName: str
    gender: Gender
    lastName: str
    status: UserStatus
