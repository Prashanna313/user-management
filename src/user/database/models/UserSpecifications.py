from sqlalchemy import and_
from user.database.models.User import User
from user.v1.endpoints.get_user.schemas.GetUserCriteria import GetUserCriteria


class UserSpecifications:
    @staticmethod
    def _and_wheres(current, to_and):
        if current is None:
            return to_and

        return and_(current, to_and)

    @staticmethod
    def create_where(criteria: GetUserCriteria):
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
