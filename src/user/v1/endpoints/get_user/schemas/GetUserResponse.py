from typing import List, Optional
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from user.schemas.Address import Address
from user.schemas import Address, Gender, UserBase, UserStatus


class User(UserBase):
    address: Optional[Address] = None
    createdBy: str
    createdOn: datetime
    dateOfBirth: date
    email: EmailStr
    firstName: str
    gender: Gender
    lastName: str
    modifiedBy: str
    modifiedOn: datetime
    status: UserStatus


class GetUserResponse(BaseModel):
    users: List[User]

