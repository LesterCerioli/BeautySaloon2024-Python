from typing import Optional
from uuid import uuid4

from domain.models.customer import Customer
from value_objects.telephone import Telephone

class CreateCustomerCommand:
    def __init__(self, id: Optional[str] = None):
        self.id: str = id or str(uuid4())
        self.customer_name: Optional[str] = None
        self.email: Optional[str] = None
        self.telephone: Optional[str] = None

    def get_entity(self) -> Customer:
        return Customer(
            customer_name=self.customer_name,
            email=self.email,
            telephone=Telephone(self.telephone)  # Resolve o erro de sintaxe aqui
        )
