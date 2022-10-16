from datetime import date, datetime
from uuid import UUID
from user_management.database.models import Gender, UserStatus
from .....utils.Randomizer import Randomizer


class RandomUserAttributes:
    def __init__(self) -> None:
        self.created_by: str = Randomizer.random_str()
        self.created_on: datetime = Randomizer.random_datetime()
        self.date_of_birth: date = Randomizer.random_date()
        # document: Optional[UserDocument] = Field(sa_column=Column("document", JSON))
        self.gender: Gender = Randomizer.random_enum(Gender)
        self.email: str = Randomizer.random_str()
        self.first_name: str = Randomizer.random_str()
        self.id: UUID = Randomizer.random_uuid()
        self.last_name: str = Randomizer.random_str()
        self.modified_by: str = Randomizer.random_str()
        self.modified_on: datetime = Randomizer.random_datetime()
        self.row_version: str = Randomizer.random_str()
        self.status: UserStatus = Randomizer.random_enum(UserStatus)