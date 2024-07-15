


from dataclasses import field
from typing import Optional
from uuid import UUID, uuid4


from uuid import UUID, uuid4
from datetime import date, time
from pydantic import BaseModel, Field # type: ignore
from typing import Optional
from .models import Appointment, Customer # type: ignore

class CreateAppointmentCommand(BaseModel):
    id: UUID = Field(default_factory=uuid4, init=False)
    client_name: str
    appointment_date: date
    appointment_time: time
    attendant_name: str
    customer_id: UUID

    def get_entity(self, customer: Customer) -> Appointment:
        return Appointment(
            client_name=self.client_name,
            appointment_date=self.appointment_date,
            appointment_time=self.appointment_time,
            attendant_name=self.attendant_name,
            customer=customer
        )



def create_appointment(command: CreateAppointmentCommand):
    # Retrieve the customer from the database
    customer = db.session.query(Customer).filter(Customer.id == command.customer_id).first() # type: ignore
    if not customer:
        raise ValueError("Customer not found")
    
    # Create the appointment entity
    appointment = command.get_entity(customer)
    
    # Add the appointment to the session and commit
    db.session.add(appointment) # type: ignore
    db.session.commit() # type: ignore

