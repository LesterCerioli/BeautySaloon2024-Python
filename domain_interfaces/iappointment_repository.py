from abc import ABC, abstractmethod
from datetime import date, time

class IAppointmentRepository(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def get_client_name(self) -> str:
        pass

    @abstractmethod
    def set_client_name(self, client_name: str):
        pass

    @abstractmethod
    def get_appointment_date(self) -> date:
        pass

    @abstractmethod
    def set_appointment_date(self, appointment_date: date):
        pass

    @abstractmethod
    def get_appointment_time(self) -> time:
        pass

    @abstractmethod
    def set_appointment_time(self, appointment_time: time):
        pass

    @abstractmethod
    def get_attendant_name(self) -> str:
        pass

    @abstractmethod
    def set_attendant_name(self, attendant_name: str):
        pass

    @abstractmethod
    def get_customer_id(self) -> str:
        pass
