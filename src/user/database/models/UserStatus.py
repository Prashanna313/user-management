from enum import Enum


class UserStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    class Config:
        orm_mode = True
