

from typing import Optional
from venv import logger
from tenacity import before_sleep_log, retry, stop_after_attempt, wait_exponential
from application.handlers.attendants.createattendantcommand import CreateAttendantCommand
from application.services.contracts.iatteandantappservice import IAttendantAppService
from application.viewmodels import attendantviewmodel
from domain.contracts.iattendantrepository import IAttendantRepository


class AttendantAppService(IAttendantAppService):
    def __init__(self, attendant_repository: IAttendantRepository):
        self._attendant_repository = attendant_repository

    async def get_by_attendant_name(self, attendant_name: str) -> Optional[AttendantViewModel]:
        attendant = await self._attendant_repository.get_by_attendant_name(attendant_name)
        if attendant:
            return attendantviewmodel.from_orm(attendant)
        return None

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        before_sleep=before_sleep_log(logger, "INFO"),
        reraise=True
    )
    async def save(self, command_create: CreateAttendantCommand) -> None:
        await self._attendant_repository.add(command_create.to_entity())
        logger.info("Attendant added successfully.")
