from typing import List
from unittest import TestCase
from fastapi.testclient import TestClient
from user.main import app
from ....fixtures.TestFixture import TestFixture
from ....fixtures.UserTestFixture import UserTestFixture
from .TestContext import TestContext


class TestsBase(TestCase):
    def setUp(self) -> None:
        self.client: TestClient = TestClient(app)
        return super().setUp()

    def setup_fixtures(self, context: TestContext) -> List[TestFixture]:
        return [
            UserTestFixture(context.existing_user),
        ]

    def tearDown(self) -> None:
        return super().tearDown()
