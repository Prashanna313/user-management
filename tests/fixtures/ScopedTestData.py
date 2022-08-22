from typing import Sequence
from .TestFixture import TestFixture


class ScopedTestData:
    __test__ = False

    def __init__(self, test_data_fixtures: Sequence[TestFixture]):
        self._test_data_fixtures = test_data_fixtures

    def __enter__(self):
        for fixture in self._test_data_fixtures:
            if fixture._status == TestFixture.Status.not_applied:
                fixture.apply()

        return self

    def __exit__(self, _exc_type, _exc_value, _exc_traceback):
        for fixture in self._test_data_fixtures[::-1]:
            if fixture._status == TestFixture.Status.applied:
                try:
                    fixture.revert()
                except Exception as exception:  # pylint: disable=broad-except
                    print(f'  exception reverting fixture: {exception}')
