from dataclasses import dataclass
from typing import Optional
import re

@dataclass(frozen=True)
class Telephone:
    telephone_number: str
    telephone_region: str

    def __post_init__(self):
        if not self._is_valid_telephone(self.telephone_number):
            raise ValueError("Invalid telephone number")
    
    @staticmethod
    def _is_valid_telephone(telephone: str) -> bool:
        # Remove non-digit characters
        shorten_num = re.sub(r"[^0-9]", "", telephone)

        # Validate the length of the telephone number
        if len(shorten_num) == 13:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.telephone_number} ({self.telephone_region})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Telephone):
            return False
        return (self.telephone_number == other.telephone_number and
                self.telephone_region == other.telephone_region)

    def __hash__(self) -> int:
        return hash((self.telephone_number, self.telephone_region))

    def get_equality_components(self) -> list[str]:
        # Return components used to determine equality
        return [self.telephone_number, self.telephone_region]
