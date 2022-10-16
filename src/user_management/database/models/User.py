from datetime import date, datetime
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import JSON, Column, Enum, Field
from user_management.database.models.BaseModel import BaseModel
from user_management.database.models.Gender import Gender
from user_management.database.models.UserDocument import UserDocument
from user_management.database.models.UserStatus import UserStatus


class User(BaseModel, table=True):
    __tablename__: str = "user"
    date_of_birth: date
    document: Optional[UserDocument] = Field(sa_column=Column("document", JSON))
    email: str
    first_name: str
    gender: Gender = Field(sa_column=Column("gender", Enum(Gender)), nullable=False)
    id: UUID = Field(default_factory=uuid4, nullable=False, primary_key=True)
    last_name: str
    row_version: str = Field(default=str(uuid4()), nullable=False)
    status: UserStatus = Field(sa_column=Column("status", Enum(UserStatus)), nullable=False)

    class Config:
        arbitrary_types_allowed = True
