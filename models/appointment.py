from sqlalchemy import Column, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    client_name = Column(String(80), nullable=False)
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    attendant_name = Column(String(80), nullable=False)
    customer_id = Column(String(36), ForeignKey('customers.id'), nullable=False)
    customer = relationship('Customer', backref='appointments')

    def __init__(self, client_name, appointment_date, appointment_time, attendant_name, customer):
        self.client_name = client_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.attendant_name = attendant_name
        self.customer = customer
        self.customer_id = customer.id
        
    def __repr__(self):
        return f"<Appointment(id='{self.id}', client_name='{self.client_name}', appointment_date='{self.appointment_date}', appointment_time='{self.appointment_time}', attendant_name='{self.attendant_name}', customer_id='{self.customer_id}')>"
