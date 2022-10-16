from typing import Optional
from pydantic import BaseModel


class Address(BaseModel):
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    country: str
