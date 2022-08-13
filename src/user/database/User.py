from datetime import date, datetime
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import JSON, Column, Enum, Field
from user.database.BaseModel import BaseModel
from user.database.UserDocument import UserDocument
from user.database.UserStatus import UserStatus


class User(BaseModel, table=True):
    __tablename__: str = "user"
    created_by: str
    created_on: datetime
    date_of_birth: date
    document: Optional[UserDocument] = Field(sa_column=Column("document", JSON))
    email: str
    first_name: str
    id: UUID = Field(default=uuid4(), primary_key=True)
    last_name: str
    modified_by: str
    modified_on: datetime
    row_version: str
    status: UserStatus = Field(sa_column=Column("status", Enum(UserStatus)))
