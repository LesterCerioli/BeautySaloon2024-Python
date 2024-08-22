

from abc import abstractmethod
from sre_parse import State


class IStateRepository(State):
    @abstractmethod
    async def get_by_state_name(self, state_name: str) -> State:
        pass

    @abstractmethod
    async def get_by_uf(self, uf: str) -> State:
        pass

    @abstractmethod
    async def get_list(self) -> List[State]:
        pass

    @abstractmethod
    async def add(self, state: State) -> None:
        pass

    @abstractmethod
    def update(self, state: State) -> None:
        pass

    @abstractmethod
    def remove(self, state: State) -> None:
        pass