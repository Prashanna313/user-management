from user_management.database.models import Gender as DomainGender
from user_management.mappers.enum_mapper import EnumMapper
from user_management.schemas.Gender import Gender as ApiGender


class GenderEnumMapper(EnumMapper[DomainGender]):
    _enum_type = DomainGender
    _map = {
        DomainGender.MALE: ApiGender.MALE,
        DomainGender.FEMALE: ApiGender.FEMALE,
        DomainGender.OTHER: ApiGender.OTHER
    }
