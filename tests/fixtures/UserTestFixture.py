from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from user.database.models import User
from .TestFixture import TestFixture


class UserTestFixture(TestFixture):

    def __init__(self, users: List[User]):
        self.row_objects = users
        # self._status = TestFixture.Status.not_applied
        super().__init__()

    @classmethod
    def get_by_id(cls, id_: UUID) -> User:
        db: Session = cls.session
        return db.query(User).whereclause(User.id == id_)

    # @classmethod
    # def get_by_ids(cls, application_ids: List[UUID], repository_context: RepositoryEngineContext) -> List[Application]:
    #     table = cls.table(repository_context.engine)
    #     query = table.select().where(table.c.id.in_(application_ids))
    #     results = repository_context.connection.execute(query).fetchall()

    #     return list(map(ApplicationRepository.model_from_record, results))

    def apply(self, **kwargs):
        db = yield self.session
        for item in self.row_objects:
            db.add(item)
        db.commit()
        db.refresh(self.row_objects)
        self._status = TestFixture.Status.applied

        super().apply()

    def revert(self, **kwargs):
        # db = yield self.session
        # db.delete(self.row_objects)
        # db.commit()
        # db.refresh(self.row_objects)
        self._status = TestFixture.Status.reverted
        super().revert()
