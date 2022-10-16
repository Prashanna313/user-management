from enum import Enum
from typing import Dict, Generic, Type, TypeVar, cast

EnumBase = TypeVar("EnumBase", bound=Enum)


class EnumMapper(Generic[EnumBase]):
    """
    Generic class which you can derive from for simple mapping enums to strings.
    Its main use is to map from an incoming request swagger enum string to an
    internal domain Enum type.
    """
    _enum_type: Type[EnumBase]
    _map: Dict[Enum, str] = {}

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
