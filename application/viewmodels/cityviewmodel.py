

from dataclasses import Field
from typing import Optional
from uuid import UUID, uuid4
from wsgiref.validate import validator


class CityViewModel:
    id: UUID = Field(default_factory=uuid4)
    city_name: Optional[str] = Field(..., title="Nome da Cidade")

    @validator('city_name')
    def city_name_required(cls, value):
        if not value:
            raise ValueError("Informe o nome da cidade.")
        return value

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True