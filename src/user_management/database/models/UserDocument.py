from __future__ import annotations
from typing import Any, Dict, Optional
from sqlmodel import SQLModel


class UserDocument(SQLModel, table=False):
    address_line_1: str
    address_line_2: Optional[str]
    city: str
    country: str

    class Config:
        orm_mode = True

    @classmethod
    def from_record(cls, record: Dict[str, Any]) -> UserDocument:
        return UserDocument(
            address_line_1=record["address_line_1"],
            address_line_2=record["address_line_2"],
            city=record["city"],
            country=record["country"])
