import uuid
from datetime import datetime, timezone
from typing import List, Optional

from application.viewmodels.attendantviewmodel import Attendant
from domain.models.customer import Customer

class Appointment:
    def __init__(self, 
                 date: Optional[datetime] = None, 
                 appointment_hour: Optional[datetime] = None):
        self.id = uuid.uuid4()  # Geração automática do GUID
        self.date = date if date else datetime.now()  # Se não fornecido, usa a data atual
        self.appointment_hour = appointment_hour if appointment_hour else datetime.now(timezone.utc)
        self._attendants: List[Attendant] = []  # Lista de atendentes
        self._customers: List[Customer] = []  # Lista de clientes

    @property
    def attendants(self) -> List['Attendant']:
        return self._attendants

    @property
    def customers(self) -> List['Customer']:
        return self._customers

    def add_attendant(self, attendant: 'Attendant') -> None:
        """
        Adiciona um novo atendente à lista de atendentes.
        """
        self._attendants.append(attendant)

    def add_customer(self, customer: 'Customer') -> None:
        """
        Adiciona um novo cliente à lista de clientes.
        """
        self._customers.append(customer)

    def remove_attendant(self, attendant: 'Attendant') -> None:
        """
        Remove um atendente da lista de atendentes.
        """
        self._attendants.remove(attendant)

    def remove_customer(self, customer: 'Customer') -> None:
        """
        Remove um cliente da lista de clientes.
        """
        self._customers.remove(customer)
