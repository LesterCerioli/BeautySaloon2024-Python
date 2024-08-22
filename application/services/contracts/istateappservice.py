

from abc import abstractmethod
from typing import Optional

from application.handlers.states.createstatecommand import CreateStateCommand
from application.viewmodels.stateviewmodel import StateViewModel


class IStateAppService:
    @abstractmethod
    async def get_by_state_name(self, state_name: str) -> Optional[StateViewModel]:
        """
        Retrieve a state by its name.

        :param state_name: The name of the state.
        :return: An instance of StateViewModel or None if not found.
        """
        pass

    @abstractmethod
    async def get_by_uf(self, uf: str) -> Optional[StateViewModel]:
        """
        Retrieve a state by its UF (state abbreviation).

        :param uf: The UF of the state.
        :return: An instance of StateViewModel or None if not found.
        """
        pass

    @abstractmethod
    async def save(self, command_create: CreateStateCommand) -> None:
        """
        Save a new state.

        :param command_create: An instance of CreateStateCommand containing state details.
        """
        pass