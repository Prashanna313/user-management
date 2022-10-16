from datetime import date
from typing import Optional
from pydantic import EmailStr
from user_management.schemas.Address import Address
from user_management.schemas.Gender import Gender
from user_management.schemas.UserBase import UserBase
from user_management.schemas.UserStatus import UserStatus


class CreateUserRequest(UserBase):
    address: Optional[Address] = None
    dateOfBirth: date
    email: EmailStr
    firstName: str
    gender: Gender
    lastName: str
    status: UserStatus
