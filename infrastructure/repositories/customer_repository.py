

from typing import List, Optional
from sqlalchemy.orm import Session
from models.customer import Customer
from domain_interfaces.icustomer_repository import ICustomerRepository

class CustomerRepository(ICustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_customer(self, customer_name: str, telephone_number: str, email_address: Optional[str] = None) -> Customer:
        customer = Customer(
            _customer_name=customer_name,
            _telephone_number=telephone_number,
            email_address=email_address
        )
        self.session.add(customer)
        self.session.commit()
        return customer

    def get_customer_by_telephone(self, telephone_number: str) -> Optional[Customer]:
        return self.session.query(Customer).filter_by(_telephone_number=telephone_number).first()

    def update_customer(self, customer_id: str, customer_name: Optional[str] = None, telephone_number: Optional[str] = None, email_address: Optional[str] = None) -> Optional[Customer]:
        customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            if customer_name:
                customer._customer_name = customer_name
            if telephone_number:
                customer._telephone_number = telephone_number
            if email_address:
                customer.email_address = email_address
            self.session.commit()
        return customer

    def delete_customer(self, customer_id: str) -> Optional[Customer]:
        customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            self.session.delete(customer)
            self.session.commit()
        return customer

    def list_customers(self) -> List[Customer]:
        return self.session.query(Customer).all()
