from typing import List
from pydantic import BaseModel
from user.schemas import UserBase


class GetUserResponse(BaseModel):
    users: List[UserBase]
