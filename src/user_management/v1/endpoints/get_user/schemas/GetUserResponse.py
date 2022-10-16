from typing import List
from pydantic import BaseModel
from user_management.schemas import UserBase


class GetUserResponse(BaseModel):
    users: List[UserBase]
