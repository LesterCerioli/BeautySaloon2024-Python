

from abc import abstractmethod
from domain.models.city import City


class ICityRepository(City):
    @abstractmethod
    async def get_by_city_name(self, city_name: str) -> Optional[City]:
        """
        Retrieve a city by its name.
        """
        pass

    @abstractmethod
    async def get_list(self) -> List[City]:
        """
        Retrieve a list of all cities.
        """
        pass

    @abstractmethod
    async def add(self, city: City) -> None:
        """
        Add a new city.
        """
        pass

    @abstractmethod
    def update(self, city: City) -> None:
        """
        Update an existing city.
        """
        pass

    @abstractmethod
    def remove(self, city: City) -> None:
        """
        Remove a city.
        """
        pass