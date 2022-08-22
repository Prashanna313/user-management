from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from user.core.config import settings


class TestFixture:
    __test__ = False

    class Status(Enum):
        not_applied = 1
        applied = 2
        reverted = 3

    def __init__(self):
        self._status = TestFixture.Status.not_applied
        self.session: Session = self.create_session()

    @classmethod
    def create_session(cls) -> Session:
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
        session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return session

    def revert_status(self):
        self._status = TestFixture.Status.reverted

    @property
    def status(self) -> Status:
        return self._status

    def revert(self, **_):
        self.revert_status()

    def apply(self, **_):
        self._status = TestFixture.Status.applied
