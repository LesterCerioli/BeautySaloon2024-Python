

from datetime import datetime
from typing import Optional
from venv import logger

from tenacity import before_sleep_log, retry, stop_after_attempt, wait_exponential
from application.handlers.appointments.createappointmentcommmand import CreateAppointmentCommand
from application.services.contracts.iappointmentappservice import IAppointmentAppService
from application.viewmodels.appointmentviewmodel import AppointmentViewModel
from domain.contracts.iappointmentrepository import IAppoitnmentRepository


class AppointmentAppService(IAppointmentAppService):
    def __init__(self, appointment_repository: IAppoitnmentRepository):
        self._appointment_repository = appointment_repository

    async def get_by_appointment_hour(self, appointment_hour: Optional[datetime]) -> Optional[AppointmentViewModel]:
        appointment = await self._appointment_repository.get_by_appointment_hour(appointment_hour)
        if appointment:
            return AppointmentViewModel.from_orm(appointment)
        return None

    async def get_by_date(self, date: Optional[datetime]) -> Optional[AppointmentViewModel]:
        appointment = await self._appointment_repository.get_by_date(date)
        if appointment:
            return AppointmentViewModel.from_orm(appointment)
        return None

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        before_sleep=before_sleep_log(logger, "INFO"),
        reraise=True
    )
    async def save(self, command: CreateAppointmentCommand) -> None:
        await self._appointment_repository.add(command.to_entity())
        logger.info("Appointment added successfully.")