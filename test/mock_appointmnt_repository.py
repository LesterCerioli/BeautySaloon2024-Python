

from datetime import date
import time

from domain_interfaces.iappointment_repository import IAppointmentRepository


class MockAppointmentRepository(IAppointmentRepository):
    def __init__(self):
        self._id = "1"
        self._client_name = ""
        self._appointment_date = date.today()
        self._appointment_time = time(12, 0)
        self._attendant_name = ""
        self._customer_id = "123"

    def get_id(self) -> str:
        return self._id

    def get_client_name(self) -> str:
        return self._client_name

    def set_client_name(self, client_name: str):
        self._client_name = client_name

    def get_appointment_date(self) -> date:
        return self._appointment_date

    def set_appointment_date(self, appointment_date: date):
        self._appointment_date = appointment_date

    def get_appointment_time(self) -> time:
        return self._appointment_time

    def set_appointment_time(self, appointment_time: time):
        self._appointment_time = appointment_time

    def get_attendant_name(self) -> str:
        return self._attendant_name

    def set_attendant_name(self, attendant_name: str):
        self._attendant_name = attendant_name

    def get_customer_id(self) -> str:
        return self._customer_id