from uuid import uuid4
from .app import db  # type: ignore
from abc import ABC, abstractmethod

class ICustomerRepository(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def get_customer_name(self) -> str:
        pass

    @abstractmethod
    def set_customer_name(self, customer_name: str):
        pass

    @abstractmethod
    def get_telephone_number(self) -> str:
        pass

    @abstractmethod
    def set_telephone_number(self, telephone_number: str):
        pass
