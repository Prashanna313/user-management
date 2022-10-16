from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import SQLModel


class BaseModel(SQLModel, table=False):
    created_by: str = "system"
    created_on: datetime
    id: UUID
    modified_by: str = "system"
    modified_on: datetime = datetime.now()
    row_version: str

    class Config:
        orm_mode = True
