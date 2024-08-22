

from datetime import datetime
from typing import Optional
from uuid import uuid4

from domain.models.appointment import Appointment


class CreateAppointmentCommand:
    def __init__(self):
        self.id: str = str(uuid4())
        self.date: Optional[datetime] = None
        self.appointment_hour: Optional[datetime] = None

    def get_entity(self) -> Appointment:
        # Define the current date and time if not provided
        date_value = self.date or datetime.now()
        appointment_hour_value = self.appointment_hour or datetime.now(timezone.utc)
        
        # Returns an instance of the AppointmentEntity
        return Appointment(date_value, appointment_hour_value)