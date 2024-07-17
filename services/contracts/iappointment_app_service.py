

from abc import abstractmethod
from datetime import date, time
from typing import List, Optional
from uuid import UUID

from application.handlers.appointments.create_appointment_command import CreateAppointmentCommand
from models.appointment import Appointment
from models.customer import Customer




class IAppointmentAppService(ABC):
    @abstractmethod
    def create_appointment(
        self,
        customer_name: str,
        appointment_date: date,
        appointment_time: time,
        attendant_name: str,
        customer_id: UUID
    ) -> Appointment:
        """Creates a new appointment"""
        pass
    
    @abstractmethod
    def get_appointments_by_date(self, appointment_date: date) -> List[Appointment]:
        """Retrieves appointments by appointment date"""
        pass
    
    @abstractmethod
    def get_appointments_by_time(self, appointment_time: time) -> List[Appointment]:
        """Retrieves appointments by appointment time"""
        pass
    
    @abstractmethod
    def update_appointment(
        self,
        appointment_id: UUID,
        customer_name: Optional[str] = None,
        appointment_date: Optional[date] = None,
        appointment_time: Optional[time] = None,
        attendant_name: Optional[str] = None,
        customer: Optional[Customer] = None
    ) -> Optional[Appointment]:
        """Updates an existing appointment"""
        pass

    @abstractmethod
    def delete_appointment(self, appointment_id: UUID) -> bool:
        """Deletes an appointment by ID"""
        pass
