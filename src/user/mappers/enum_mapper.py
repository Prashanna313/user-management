from enum import Enum
from typing import Dict, Generic, Type, TypeVar, cast

EnumBase = TypeVar("EnumBase", bound=Enum)


class EnumMapper(Generic[EnumBase]):
    """
    Generic class which you can derive from for simple mapping enums to strings.
    Its main use is to map from an incoming request swagger enum string to an
    internal domain Enum type.

    Example
    -------
    ```
        class DomainEnum(Enum):
            DOMAIN_VALUE_1 = 1
            DOMAIN_VALUE_2 = 2

        class SwaggerEnum:
            SWAGGER_VALUE_1 = "v1"
            SWAGGER_VALUE_2 = "v2"

        class DomainEnumMapper(EnumMapper[DomainEnum]):
            _enum_type = DomainEnum
            _map = {
                DomainEnum.DOMAIN_VALUE_1: SwaggerEnum.SWAGGER_VALUE_1,
                DomainEnum.DOMAIN_VALUE_2: SwaggerEnum.SWAGGER_VALUE_2
            }

        assert DomainEnumMapper.from_domain(DomainEnum.DOMAIN_VALUE_1) == SwaggerEnum.SWAGGER_VALUE_1
        assert DomainEnumMapper.to_domain(SwaggerEnum.SWAGGER_VALUE_2) == DomainEnum.DOMAIN_VALUE_2
    ```
    """
    _enum_type: Type[EnumBase]
    _map: Dict[Enum, str] = {}  # TODO: ideally we want this as EnumBase, but dict is an invariant

    @classmethod
    def from_domain(cls, domain: EnumBase) -> str:
        """
        Map from the domain enum to the mapped api string.

        Parameters
        ----------
        :param EnumBase domain: the domain enum to map from
        :return: the mapped enum string value
        :rtype: str
        """
        return cls._map[domain]

    @classmethod
    def to_domain(cls, api: str) -> EnumBase:
        """
        Map from the api string to the mapped domain enum.

        Parameters
        ----------
        :param str api: the api string to map from
        :return: the mapped domain enum value
        :rtype: EnumBase
        """
        values = list(cls._map.values())

        if api not in values:
            raise ValueError(f"unknown {cls._enum_type} value '{api}'")

        return cast(EnumBase, list(cls._map.keys())[values.index(api)])
