

from dataclasses import Field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from wsgiref.validate import validator


class AppointmentViewModel:
    id: UUID = Field(default_factory=uuid4)
    date: Optional[datetime] = Field(..., title="Data de Agendamento")
    appointment_hour: Optional[datetime] = Field(..., title="Hora de Agendamento")

    @validator('date')
    def date_required(cls, value):
        if value is None:
            raise ValueError('Informe a data de agendamento.')
        return value

    @validator('appointment_hour')
    def appointment_hour_required(cls, value):
        if value is None:
            raise ValueError('Informe a hora de agendamento.')
        return value

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True