from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel # type: ignore
from dataclasses import dataclass, field

class CustomerEntity(BaseModel):
    customer_name: Optional[str]
    telephone_number: Optional[str]
    
class CreateCustomerCommand(BaseModel):
    id: UUID = field(default_factory=uuid4, init=False)
    customer_name: Optional[str] = None
    telephone_number: Optional[str] = None
    
    def get_entity(self) -> CustomerEntity:
        return CustomerEntity(
            customer_name=self.customer_name,
            telephone_number=self.telephone_number
        )
