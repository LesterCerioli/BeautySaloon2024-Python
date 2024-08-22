

from abc import abstractmethod
from domain.models.saloon import Saloon


class ISaloonRepository(Saloon):
    @abstractmethod
    async def get_by_fantasy_name(self, fantasy_name: str) -> Saloon:
        pass

    @abstractmethod
    async def get_by_address(self, address: Address) -> Saloon:
        pass

    @abstractmethod
    async def get_by_district(self, district: District) -> Saloon:
        pass

    @abstractmethod
    async def get_list(self) -> List[Saloon]:
        pass

    @abstractmethod
    async def add(self, saloon: Saloon) -> None:
        pass

    @abstractmethod
    def update(self, saloon: Saloon) -> None:
        pass

    @abstractmethod
    def remove(self, saloon: Saloon) -> None:
        pass