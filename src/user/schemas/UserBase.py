from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr
from user.schemas.Address import Address
from user.schemas.Gender import Gender
from user.schemas.UserStatus import UserStatus


class UserBase(BaseModel):
    address: Optional[Address] = None
    dateOfBirth: date
    email: EmailStr
    firstName: str
    gender: Gender
    lastName: str
    status: UserStatus
