from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import SQLModel


class BaseModel(SQLModel, table=False):
    created_by: str
    created_on: datetime
    id: UUID
    modified_by: str
    modified_on: datetime
    row_version: str = str(uuid4())

    class Config:
        orm_mode = True
