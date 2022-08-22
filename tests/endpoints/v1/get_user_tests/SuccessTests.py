from tests.endpoints.v1.get_user_tests.TestContext import TestContext
from .test_base import TestsBase
from ....fixtures.ScopedTestData import ScopedTestData


class SuccessTests(TestsBase):
    def test_WHEN_get_user_called_THEN_fetched_ALL_users(self):
        context = TestContext()
        test_fixtures = self.setup_fixtures(context=context)
        with ScopedTestData(test_fixtures):
            result = self.client.get("/users")
        assert result.status_code == 200
