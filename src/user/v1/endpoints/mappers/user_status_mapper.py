from user.database.models import UserStatus as DomainUserStatus
from user.mappers.enum_mapper import EnumMapper
from user.schemas.UserStatus import UserStatus as ApiUserStatus


class UserStatusEnumMapper(EnumMapper[DomainUserStatus]):
    _enum_type = DomainUserStatus
    _map = {
        DomainUserStatus.ACTIVE: ApiUserStatus.ACTIVE,
        DomainUserStatus.INACTIVE: ApiUserStatus.INACTIVE
    }
