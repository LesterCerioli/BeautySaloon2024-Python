

from abc import abstractmethod
from email.headerregistry import Address
from typing import Optional

from application.handlers.saloons.createsalooncommand import CreateSaloonCommand
from application.viewmodels.saloonviewmodel import SaloonViewModel
from value_objects.district import District


class ISaloonAppService:
    @abstractmethod
    async def get_by_district(self, district: District) -> Optional[SaloonViewModel]:
        """
        Retrieve a saloon view model by the district.

        :param district: An instance of District representing the saloon's district.
        :return: An instance of SaloonViewModel representing the saloon, or None if not found.
        """
        pass

    @abstractmethod
    async def get_by_fantasy_name(self, fantasy_name: str) -> Optional[SaloonViewModel]:
        """
        Retrieve a saloon view model by the fantasy name.

        :param fantasy_name: The fantasy name of the saloon.
        :return: An instance of SaloonViewModel representing the saloon, or None if not found.
        """
        pass

    @abstractmethod
    async def get_by_address(self, address: Address) -> Optional[SaloonViewModel]:
        """
        Retrieve a saloon view model by the address.

        :param address: An instance of Address representing the saloon's address.
        :return: An instance of SaloonViewModel representing the saloon, or None if not found.
        """
        pass

    @abstractmethod
    async def save(self, command_create: CreateSaloonCommand) -> None:
        """
        Save a new saloon using the provided command.

        :param command_create: An instance of CreateSaloonCommand containing saloon creation details.
        """
        pass