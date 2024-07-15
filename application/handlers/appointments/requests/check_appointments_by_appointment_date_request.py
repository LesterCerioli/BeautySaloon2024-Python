
from pydantic import BaseModel
from datetime import date, time
from uuid import uuid4

class CheckAppointmentsByAppointmentDateRequest(BaseModel):
    id: str
    appointment_date: date
    appointment_time: time

    def __init__(self, appointment_date: date, appointment_time: time):
        super().__init__(id=str(uuid4()), appointment_date=appointment_date, appointment_time=appointment_time)
        
def create_appointment_request(appointment_date: date, appointment_time: time):
    request = CheckAppointmentsByAppointmentDateRequest(
        appointment_date=appointment_date,
        appointment_time=appointment_time
    )
    
    print(request.id)
    print(request.appointment_date)
    print(request.appointment_time)
    

    
    


