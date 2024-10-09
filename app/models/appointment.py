import uuid
from typing import List, Optional
from pydantic import BaseModel, Field
import datetime

from app.models.attendant import Attendant
from app.models.customer import Customer

# Define the response model with Pydantic
class Appointment(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)  # Generate a UUID by default
    date: Optional[datetime.datetime] = None
    appointment_hour: Optional[datetime.datetime] = None
    attendants: List["Attendant"] = []  # List of attendants (not null by default)
    customer: Optional["Customer"] = None  # Optional customer

    class Config:
        # Ensure datetime fields are handled correctly
        anystr_strip_whitespace = True
        json_encoders = {
            uuid.UUID: lambda v: str(v),  # Converts UUID to string
            datetime.datetime: lambda v: v.isoformat()  # Converts datetime to ISO format
        }

    def __repr__(self):
        return f"Appointment(id={self.id}, date={self.date}, appointment_hour={self.appointment_hour}, customer={self.customer})"
