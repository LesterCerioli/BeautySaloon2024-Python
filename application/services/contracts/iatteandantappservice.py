

from abc import abstractmethod

from application.handlers.attendants.createattendantcommand import CreateAttendantCommand
from application.viewmodels import attendantviewmodel


class IAttendantAppService:
    @abstractmethod
    async def get_by_attendant_name(self, attendant_name: str) -> 'attendantviewmodel':
        pass

    @abstractmethod
    async def save(self, command_create: 'CreateAttendantCommand') -> None:
        pass