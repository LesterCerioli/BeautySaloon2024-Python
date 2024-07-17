from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy.orm import Session

from models.customer import Customer

class ICustomerRepository(ABC):
    
    @abstractmethod
    def create_customer(self, customer_name: str, telephone_number: str, email_address: Optional[str] = None) -> Customer:
        pass
    
    @abstractmethod
    def get_customer_by_telephone(self, telephone_number: str) -> Optional[Customer]:
        pass
    
    @abstractmethod
    def get_customer_by_customer_name(self, customer_name: str) -> Optional[Customer]:
        pass
    
    @abstractmethod
    def update_customer(self, customer_id: str, customer_name: Optional[str] = None, telephone_number: Optional[str] = None, email_address: Optional[str] = None) -> Optional[Customer]:
        pass
    
    @abstractmethod
    def delete_customer(self, customer_id: str) -> Optional[Customer]:
        pass
    
    @abstractmethod
    def list_customers(self) -> List[Customer]:
        pass
