

from datetime import date, time
from typing import Optional
from uuid import UUID
from domain_interfaces.iappointment_repository import IAppointmentRepository
from models.appointment import Appointment
from models.customer import Customer
from services.contracts.iappointment_app_service import IAppointmentAppService


class AppointmentAppService(IAppointmentAppService):
    def __init__(self, repository: IAppointmentRepository):
        self.repository = repository

    def create_appointment(
        self,
        customer_name: str,
        appointment_date: date,
        appointment_time: time,
        attendant_name: str,
        customer_id: UUID
    ) -> Appointment:
        customer = self.repository.get_customer_by_id(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        appointment = Appointment(
            customer_name=customer_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            attendant_name=attendant_name,
            customer=customer
        )
        self.repository.add_appointment(appointment)
        return appointment

    def get_appointments_by_date(self, appointment_date: date) -> List[Appointment]:
        return self.repository.get_by_appointment_date(appointment_date)

    def get_appointments_by_time(self, appointment_time: time) -> List[Appointment]:
        return self.repository.get_by_appointment_time(appointment_time)

    def update_appointment(
        self,
        appointment_id: UUID,
        customer_name: Optional[str] = None,
        appointment_date: Optional[date] = None,
        appointment_time: Optional[time] = None,
        attendant_name: Optional[str] = None,
        customer: Optional[Customer] = None
    ) -> Optional[Appointment]:
        appointment = self.repository.get_appointment_by_id(appointment_id)
        if not appointment:
            return None
        
        if customer_name:
            appointment.customer_name = customer_name
        if appointment_date:
            appointment.appointment_date = appointment_date
        if appointment_time:
            appointment.appointment_time = appointment_time
        if attendant_name:
            appointment.attendant_name = attendant_name
        if customer:
            appointment.customer = customer
        
        self.repository.update_appointment(appointment)
        return appointment

    def delete_appointment(self, appointment_id: UUID) -> bool:
        return self.repository.delete_appointment(appointment_id)