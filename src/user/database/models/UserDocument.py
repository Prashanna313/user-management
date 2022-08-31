from typing import Optional
from sqlmodel import SQLModel


class UserDocument(SQLModel, table=False):
    address_line_1: str
    address_line_2: Optional[str]
    city: str
    country: str

    class Config:
        orm_mode = True
