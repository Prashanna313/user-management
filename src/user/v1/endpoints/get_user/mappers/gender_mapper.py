from user.database.models import Gender as DomainGender
from user.mappers.enum_mapper import EnumMapper
from user.schemas.Gender import Gender as ApiGender


class GenderEnumMapper(EnumMapper[DomainGender]):
    _enum_type = DomainGender
    _map = {
        DomainGender.MALE: ApiGender.MALE,
        DomainGender.FEMALE: ApiGender.FEMALE,
        DomainGender.OTHER: ApiGender.OTHER
    }
