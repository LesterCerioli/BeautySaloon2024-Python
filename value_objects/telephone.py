

from dataclasses import Field
from wsgiref.validate import validator


class Telephone(BaseModel): # type: ignore
    ddd: Field(..., min_length=2, max_length=2, regex=r'^\d{2}$') # type: ignore
    telephone_number: str = Field(..., min_length=9, max_length=9, regex=r'^\d{9}$')
    
    @validator('ddd')
    def validate_ddd(cls, v):
        if not v.isdigit():
            raise ValueError("DDD deve possuir apenas dois algarismos")
        return v
    
    @validator('telephone_number')
    def validate_telephone_number(cls, v):
        if not v.isdigit():
            raise ValueError("O número do telefone deve conter APENAS 9 dígitos.")
        return v
    def __str__(self):
        return f"({self.ddd}) {self.telephone_number}"
    
    