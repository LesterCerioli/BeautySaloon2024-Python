from uuid import uuid4

from value_objects.telephone import Telephone
from .app import db  # type: ignore


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    _customer_name = db.Column('customer_name', db.String(80), nullable=False)
    _telephone_number = db.Column('telephone_number', db.String(11), nullable=False)

    def __init__(self, customer_name: str, telephone: Telephone):
        self.id = str(uuid4())
        self.customer_name = customer_name
        self.telephone = telephone

    @property
    def customer_name(self) -> str:
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value: str):
        if not value:
            raise ValueError("O nome do cliente deve ser informado")
        self._customer_name = value

    @property
    def telephone(self) -> Telephone:
        ddd, number = self._telephone_number[:2], self._telephone_number[2:]
        return Telephone(ddd=ddd, telephone_number=number)

    @telephone.setter
    def telephone(self, value: Telephone):
        if not value:
            raise ValueError("O número de telefone deve ser informado")
        self._telephone_number = value.ddd + value.telephone_number

    def get_id(self) -> str:
        return self.id

    def get_customer_name(self) -> str:
        return self.customer_name

    def set_customer_name(self, customer_name: str):
        self.customer_name = customer_name

    def get_telephone(self) -> Telephone:
        return self.telephone

    def set_telephone(self, telephone: Telephone):
        self.telephone = telephone
