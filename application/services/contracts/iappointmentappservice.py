

from abc import abstractmethod
from datetime import datetime, timedelta
from typing import Optional

from application.handlers.appointments.createappointmentcommmand import CreateAppointmentCommand
from application.viewmodels.appointmentviewmodel import AppointmentViewModel


class IAppointmentAppService:
    @abstractmethod
    async def get_by_date(self, date: Optional[datetime]) -> 'AppointmentViewModel':
        pass

    @abstractmethod
    async def get_by_appointment_hour(self, appointment_hour: Optional[timedelta]) -> 'AppointmentViewModel':
        pass

    @abstractmethod
    async def save(self, command_create: 'CreateAppointmentCommand') -> None:
        pass
