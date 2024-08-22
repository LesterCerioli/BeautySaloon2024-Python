

from abc import abstractmethod
from domain.models.attendant import Attendant


class IAttendantRepository(Attendant):
    @abstractmethod
    async def get_by_attendant_name(self, attendant_name: str) -> Optional[Attendant]:
        """
        Retrieve an attendant by their name.
        """
        pass

    @abstractmethod
    async def get_list(self) -> List[Attendant]:
        """
        Retrieve a list of all attendants.
        """
        pass

    @abstractmethod
    async def add(self, attendant: Attendant) -> None:
        """
        Add a new attendant.
        """
        pass

    @abstractmethod
    def update(self, attendant: Attendant) -> None:
        """
        Update an existing attendant.
        """
        pass

    @abstractmethod
    def remove(self, attendant: Attendant) -> None:
        """
        Remove an attendant.
        """
        pass