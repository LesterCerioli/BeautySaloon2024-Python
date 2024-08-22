from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Address:
    address: Optional[str]
    avenue_or_street: Optional[str] = None
    number: Optional[str] = None

    def __post_init__(self):
        # Add custom initialization logic if needed
        pass

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return (self.address == other.address and
                self.avenue_or_street == other.avenue_or_street and
                self.number == other.number)

    def __hash__(self):
        return hash((self.address, self.avenue_or_street, self.number))
