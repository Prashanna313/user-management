from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from user.schemas.Gender import Gender
from user.schemas.UserStatus import UserStatus
from user.schemas.Address import Address


class UserBase(BaseModel):
    address: Optional[Address] = None
    createdBy: Optional[str] = None
    createdOn: Optional[datetime] = None
    dateOfBirth: Optional[date] = None
    email: Optional[EmailStr] = None
    firstName: Optional[str] = None
    gender: Optional[Gender] = None
    lastName: Optional[str] = None
    modifiedBy: Optional[str] = None
    modifiedOn: Optional[datetime] = None
    status: Optional[UserStatus] = None