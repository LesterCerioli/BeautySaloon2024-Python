from uuid import uuid4
from datetime import date, time
from .app import db # type: ignore

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    _customer_name = db.Column('customer_name', db.String(80), nullable=False)
    _telephone_number = db.Column('telephone_number', db.String(20), nullable=False)

    def __init__(self, customer_name: str, telephone_number: str):
        self.id = str(uuid4())
        self.customer_name = customer_name
        self.telephone_number = telephone_number

    @property
    def customer_name(self) -> str:
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value: str):
        if not value:
            raise ValueError("O nome do cliente deve ser informado")
        self._customer_name = value

    @property
    def telephone_number(self) -> str:
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, value: str):
        if not value:
            raise ValueError("O número de telefone deve ser informado")
        self._telephone_number = value
