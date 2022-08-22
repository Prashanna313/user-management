import datetime
from decimal import Decimal
from enum import Enum
import pytz
import random
from sys import maxsize
from typing import Any, Optional, Sequence, Type
from uuid import UUID, uuid4

TEXT_ENCODING_UTF8 = "utf-8"


class Randomizer:
    random.seed()

    @staticmethod
    def random_bool() -> bool:
        return Randomizer.random_from_list([False, True])

    @staticmethod
    def random_bytearray(length: int = 8, encoding: str = TEXT_ENCODING_UTF8) -> bytearray:
        to_convert = ""
        while len(to_convert) < length:
            to_convert += Randomizer.random_str()

        return bytearray(to_convert[:length], encoding)

    @staticmethod
    def random_bytes(length: int = 8, encoding: str = TEXT_ENCODING_UTF8) -> bytes:
        return bytes(Randomizer.random_bytearray(length, encoding))

    @staticmethod
    def random_complex() -> complex:
        return complex(Randomizer.random_int(), Randomizer.random_int())

    @staticmethod
    def random_datetime():
        return datetime.datetime(
            Randomizer.random_int(2000, 2050),
            Randomizer.random_int(1, 12),
            Randomizer.random_int(1, 28),
            Randomizer.random_int(0, 23),
            Randomizer.random_int(0, 59),
            Randomizer.random_int(0, 59),
            Randomizer.random_int(0, 999999),
            tzinfo=datetime.timezone.utc)

    @staticmethod
    def random_date():
        return datetime.date(
            Randomizer.random_int(2000, 2050),
            Randomizer.random_int(1, 12),
            Randomizer.random_int(1, 28))

    @staticmethod
    def random_day():
        return f"{Randomizer.random_int(2000, 2050):4}-{Randomizer.random_int(1, 12):-02}-{Randomizer.random_int(1, 28):02}"

    @staticmethod
    def random_email() -> str:
        return f"{Randomizer.random_str()[:10]}@{Randomizer.random_str()[:10]}.com.au"

    @staticmethod
    def random_enum(enum: Type[Enum]):
        enum_values = [getattr(enum, attrib) for attrib in dir(enum) if not attrib.startswith("_")]

        return Randomizer.random_from_list(enum_values)

    @staticmethod
    def random_float(minimum: float = 0.0, maximum: float = 1.0, round_to: Optional[int] = None, divisible_by: Optional[float] = None) -> float:
        if divisible_by is None:
            value = (random.random() * (maximum - minimum)) + minimum
        elif divisible_by > 0:
            start_range = int(minimum // divisible_by) + 1
            end_range = int(maximum // divisible_by) + 1
            coefficient = random.randrange(start_range, end_range)

            value = float(Decimal(str(coefficient)) * Decimal(str(divisible_by)))

        else:
            raise ValueError("divisible_by argument should be greater than 0.0")

        if round_to is None:
            return value

        return round(value, round_to)

    @staticmethod
    def random_from_list(choice: Sequence[Any]):
        return random.choice(choice)

    @staticmethod
    def random_int(minimum: int = 0, maximum: int = maxsize) -> int:
        return random.randint(minimum, maximum)

    @staticmethod
    def random_32bit_int(minimum: int = 0, maximum: int = 2147483647) -> int:
        return random.randint(minimum, maximum)

    @staticmethod
    def random_latitude():
        return random.uniform(-90, 90)

    @staticmethod
    def random_longitude():
        return random.uniform(-180, 180)

    @classmethod
    def random_phone_number(cls) -> str:
        num_digits = Randomizer.random_int(minimum=1, maximum=15)
        return "+" + "".join(str(Randomizer.random_int(minimum=0, maximum=9)) for _ in range(num_digits))

    @staticmethod
    def random_str(min_length=1, max_length=0) -> str:
        random_str = ""

        while len(random_str) < min_length:
            random_str += str(Randomizer.random_uuid())

        if max_length > 0:
            return random_str[0:max_length]

        return random_str

    @staticmethod
    def random_str_from_sequence(length: int, characters: Sequence) -> str:
        return "".join(Randomizer.random_from_list(characters) for _ in range(length))

    @staticmethod
    def random_time():
        return datetime.time(
            Randomizer.random_int(0, 23),
            Randomizer.random_int(0, 59),
            Randomizer.random_int(0, 59),
            Randomizer.random_int(0, 999999),
            tzinfo=datetime.timezone.utc)

    @staticmethod
    def random_time_of_day(include_seconds: bool = True):
        time = f"{Randomizer.random_int(0, 23):02}:{Randomizer.random_int(0, 59):02}"

        if include_seconds:
            time += f":{Randomizer.random_int(0, 59):02}"

        return time

    @staticmethod
    def random_timedelta():
        return datetime.timedelta(minutes=Randomizer.random_int(-60 * 24, 60 * 24))

    @staticmethod
    def random_timezone():
        return Randomizer.random_from_list(pytz.all_timezones)

    @staticmethod
    def random_uuid() -> UUID:
        return uuid4()
