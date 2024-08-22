from dataclasses import dataclass
from typing import Optional
import re

@dataclass(frozen=True)
class Cnpj:
    cnpj_number: str

    def __post_init__(self):
        # Validate CNPJ number during initialization
        if not self.is_valid(self.cnpj_number):
            raise ValueError("Invalid CNPJ Number")

    @property
    def cnpj_number(self) -> str:
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, value: str):
        if not self.is_valid(value):
            raise ValueError("Invalid CNPJ Number")
        object.__setattr__(self, '_cnpj_number', value)

    @staticmethod
    def is_valid(cnpj_number: str) -> bool:
        # Remove non-digit characters
        cnpj_number = re.sub(r'\D', '', cnpj_number)

        # CNPJ must have 14 digits
        if len(cnpj_number) != 14:
            return False

        # Check for repeated digits or invalid checksum
        if Cnpj.is_repeated_digits(cnpj_number) or not Cnpj.is_valid_checksum(cnpj_number):
            return False

        return True

    @staticmethod
    def is_repeated_digits(cnpj_number: str) -> bool:
        return len(set(cnpj_number)) == 1

    @staticmethod
    def is_valid_checksum(cnpj_number: str) -> bool:
        def calculate_digit(digits: str, weights: list[int]) -> int:
            sum_ = sum(int(digit) * weight for digit, weight in zip(digits, weights))
            remainder = sum_ % 11
            return 0 if remainder < 2 else 11 - remainder

        weights1 = list(range(5, 1, -1)) + list(range(9, 1, -1))
        weights2 = list(range(6, 1, -1)) + list(range(9, 1, -1))

        digit1 = calculate_digit(cnpj_number[:12], weights1)
        digit2 = calculate_digit(cnpj_number[:13], weights2)

        return int(cnpj_number[12]) == digit1 and int(cnpj_number[13]) == digit2

    def __eq__(self, other) -> bool:
        if not isinstance(other, Cnpj):
            return False
        return self.cnpj_number == other.cnpj_number

    def __hash__(self) -> int:
        return hash(self.cnpj_number)

    def __str__(self) -> str:
        return self.cnpj_number

    @classmethod
    def from_string(cls, value: str) -> 'Cnpj':
        return cls(value)

    @classmethod
    def to_string(cls, cnpj: 'Cnpj') -> str:
        return cnpj.cnpj_number
