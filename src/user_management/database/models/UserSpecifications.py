from typing import Any
from sqlalchemy import and_
from user_management.database.models.User import User
from user_management.v1.endpoints.get_user.schemas.GetUserCriteria import GetUserCriteria


class UserSpecifications:
    @staticmethod
    def _and_wheres(current: Any, to_and: Any) -> Any:
        if current is None:
            return to_and

        return and_(current, to_and)

    @staticmethod
    def create_where(criteria: GetUserCriteria) -> Any:
        where_clause = None

        if criteria.email:
            where_clause = UserSpecifications._and_wheres(
                where_clause,
                User.email == criteria.email)

        if criteria.user_ids:
            where_clause = UserSpecifications._and_wheres(
                where_clause,
                User.id.in_(criteria.user_ids))

        return where_clause
