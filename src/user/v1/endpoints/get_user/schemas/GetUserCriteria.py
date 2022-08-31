

from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID
from pydantic import EmailStr


@dataclass
class GetUserCriteria:
    email: Optional[EmailStr] = None
    user_ids: Optional[List[UUID]] = None
    skip: int = 0
    limit: int = 100
