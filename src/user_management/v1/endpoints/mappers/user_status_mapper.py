from user_management.database.models import UserStatus as DomainUserStatus
from user_management.mappers.enum_mapper import EnumMapper
from user_management.schemas.UserStatus import UserStatus as ApiUserStatus


class UserStatusEnumMapper(EnumMapper[DomainUserStatus]):
    _enum_type = DomainUserStatus
    _map = {
        DomainUserStatus.ACTIVE: ApiUserStatus.ACTIVE,
        DomainUserStatus.INACTIVE: ApiUserStatus.INACTIVE
    }
