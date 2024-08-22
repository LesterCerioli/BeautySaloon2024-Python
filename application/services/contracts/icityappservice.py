

from abc import abstractmethod

from application.handlers.cities.createcitycommand import CreateCityCommand
from application.viewmodels.cityviewmodel import CityViewModel


class ICityAppService:
    @abstractmethod
    async def get_by_city_name(self, city_name: str) -> 'CityViewModel':
        """
        Retrieve a city view model by the city name.

        :param city_name: The name of the city.
        :return: An instance of CityViewModel representing the city.
        """
        pass

    @abstractmethod
    async def save(self, command_create: 'CreateCityCommand') -> None:
        """
        Save a new city using the provided command.

        :param command_create: The command containing city creation details.
        """
        pass
