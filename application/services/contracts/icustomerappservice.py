

from abc import abstractmethod
from typing import Optional

from application.handlers.customers.createcustomercommand import CreateCustomerCommand
from application.viewmodels.customerviewmodel import CustomerViewModel
from value_objects.telephone import Telephone


class ICustomerAppService:
    @abstractmethod
    async def get_by_customer(self, customer_name: str) -> Optional[CustomerViewModel]:
        """
        Retrieve a customer view model by the customer's name.

        :param customer_name: The name of the customer.
        :return: An instance of CustomerViewModel representing the customer, or None if not found.
        """
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[CustomerViewModel]:
        """
        Retrieve a customer view model by the customer's email.

        :param email: The email of the customer.
        :return: An instance of CustomerViewModel representing the customer, or None if not found.
        """
        pass

    @abstractmethod
    async def get_by_telephone(self, telephone: Telephone) -> Optional[CustomerViewModel]:
        """
        Retrieve a customer view model by the customer's telephone.

        :param telephone: An instance of Telephone representing the customer's phone number.
        :return: An instance of CustomerViewModel representing the customer, or None if not found.
        """
        pass

    @abstractmethod
    async def save(self, command_create: CreateCustomerCommand) -> None:
        """
        Save a new customer using the provided command.

        :param command_create: An instance of CreateCustomerCommand containing customer creation details.
        """
        pass
