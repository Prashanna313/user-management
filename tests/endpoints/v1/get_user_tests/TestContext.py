from user_management.database.models.User import User
from .random_data.random_attributes import RandomUserAttributes


class TestContext:
    def __init__(self) -> None:
        self.user_context: RandomUserAttributes = RandomUserAttributes()
        self.build()

    def build(self):
        self.existing_user: User = self._setup_user()
        self.expected_response: User = self._setup_user()

    def _setup_user(self) -> User:
        return User(
            created_by=self.user_context.created_by,
            created_on=self.user_context.created_on,
            date_of_birth=self.user_context.date_of_birth,
            gender=self.user_context.gender,
            email=self.user_context.email,
            first_name=self.user_context.first_name,
            id=self.user_context.created_on,
            last_name=self.user_context.last_name,
            modified_by=self.user_context.modified_by,
            modified_on=self.user_context.modified_on,
            row_version=self.user_context.row_version,
            status=self.user_context.status)