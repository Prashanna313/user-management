from typing import Optional
from pydantic import BaseModel

class Address(BaseModel):
    addressLine_1: str
    addressLine_2: Optional[str] = None
    city: str
    country: str