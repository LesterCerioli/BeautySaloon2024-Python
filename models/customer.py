from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(String(36), primary_key=True)
    customer_name = Column(String(80), nullable=False)
    telephone_number = Column(String(20), nullable=False, unique=True)
    email_address = Column(String(120), nullable=True, unique=True)  # Adicionando o campo email_address
    
    def __init__(self, customer_name, telephone_number, email_address=None):
        self.customer_name = customer_name
        self.telephone_number = telephone_number
        self.email_address = email_address
        
    def __repr__(self):
        return f"<Customer(id='{self.id}', customer_name='{self.customer_name}', telephone_number='{self.telephone_number}', email_address='{self.email_address}')>"
