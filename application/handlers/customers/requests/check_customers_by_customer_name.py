

from dataclasses import Field
from typing import Optional, Type
from uuid import UUID

from requests import Session

from models.customer import Customer


class CheckCustomersByCustomerName(BaseModel): # type: ignore
    id: UUID = Field(default_factory=uuid4)
    customer_name: Optional[str] = None

    def __init__(self, customer_name: Optional[str] = None):
        super().__init__(customer_name=customer_name)
        
    @classmethod
    def check_customer(cls: Type['CheckCustomersByCustomerName'], session: Session, customer_name: str) -> 'CheckCustomersByCustomerName':
        customer = session.query(Customer).filter_by(_customer_name=customer_name).first()
        if customer:
            return cls(id=customer.get_id(), customer_name=customer.get_customer_name())
        else:
            return cls(customer_name=customer_name)