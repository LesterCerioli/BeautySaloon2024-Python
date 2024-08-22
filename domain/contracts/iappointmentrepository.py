
from abc import abstractmethod
from datetime import datetime
from typing import List, Optional
from domain.models.appointment import Appointment


class IAppoitnmentRepository(Appointment):
    async def get_by_date(self, date: Optional[datetime]) -> Optional[Appointment]:
        """
        Retrieve an appointment by its date.
        """
        pass
    
    @abstractmethod
    async def get_by_appointment_hour(self, appointment_hour: Optional[datetime]) -> Optional[Appointment]:
        """
        Retrieve an appointment by its appointment hour.
        """
        pass

    @abstractmethod
    async def get_list(self) -> List[Appointment]:
        """
        Retrieve a list of all appointments.
        """
        pass

    @abstractmethod
    async def add(self, appointment: Appointment) -> None:
        """
        Add a new appointment.
        """
        pass

    @abstractmethod
    def update(self, appointment: Appointment) -> None:
        """
        Update an existing appointment.
        """
        pass

    @abstractmethod
    def remove(self, appointment: Appointment) -> None:
        """
        Remove an appointment.
        """
        pass