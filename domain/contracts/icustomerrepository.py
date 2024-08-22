

from abc import abstractmethod
from domain.models.customer import Customer


class ICustomerRepository(Customer):
    @abstractmethod
    async def get_by_customer_name(self, customer_name: str) -> Optional[Customer]:
        """
        Retrieve a customer by their name.
        """
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[Customer]:
        """
        Retrieve a customer by their email.
        """
        pass

    @abstractmethod
    async def get_by_telephone(self, telephone: Telephone) -> Optional[Customer]:
        """
        Retrieve a customer by their telephone.
        """
        pass

    @abstractmethod
    async def get_list(self) -> List[Customer]:
        """
        Retrieve a list of all customers.
        """
        pass

    @abstractmethod
    async def add(self, customer: Customer) -> None:
        """
        Add a new customer.
        """
        pass

    @abstractmethod
    def update(self, customer: Customer) -> None:
        """
        Update an existing customer.
        """
        pass

    @abstractmethod
    def remove(self, customer: Customer) -> None:
        """
        Remove a customer.
        """
        pas