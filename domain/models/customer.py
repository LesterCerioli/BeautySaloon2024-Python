

from dataclasses import dataclass, field
from typing import Optional

from value_objects.telephone import Telephone

@dataclass
class Customer:
    id: str = field(default_factory=lambda: str(uuid4()))  # ID gerado automaticamente
    customer_name: Optional[str] = None
    email: Optional[str] = None
    telephone: Optional[Telephone] = None

    def __post_init__(self):
        if not self.customer_name:
            raise ValueError("Customer name cannot be empty")
        if not self.email:
            raise ValueError("Email cannot be empty")
        if not self.telephone:
            raise ValueError("Telephone cannot be empty")

    def __repr__(self):
        return (f"Customer(id={self.id}, customer_name={self.customer_name}, email={self.email}, "
                f"telephone={self.telephone})")

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return False
        return (self.customer_name == other.customer_name and
                self.email == other.email and
                self.telephone == other.telephone)

    def __hash__(self):
        return hash((self.customer_name, self.email, self.telephone))

    def get_equality_components(self):
        return [self.customer_name, self.email, self.telephone]