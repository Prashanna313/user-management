from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr
from user_management.schemas.Address import Address
from user_management.schemas.Gender import Gender
from user_management.schemas.UserStatus import UserStatus


class UserBase(BaseModel):
    address: Optional[Address] = None
    dateOfBirth: date
    email: EmailStr
    firstName: str
    gender: Gender
    lastName: str
    status: UserStatus
