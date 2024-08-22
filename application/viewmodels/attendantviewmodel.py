

from dataclasses import Field
from typing import Optional
from uuid import UUID, uuid4
from wsgiref.validate import validator


class Attendant:
    id: UUID = Field(default_factory=uuid4)
    attendant_name: Optional[str] = Field(..., title="Nome do Atendente")

    @validator('attendant_name')
    def attendant_name_required(cls, value):
        if not value:
            raise ValueError("O nome do atendente deve ser informado.")
        return value

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True