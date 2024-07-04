from uuid import uuid4
from datetime import date, time
from .app import db # type: ignore

class Appointment(db.Model):
    __tablename__ = 'appointments'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    client_name = db.Column(db.String(80), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    attendant_name = db.Column(db.String(80), nullable=False)
    customer_id = db.Column(db.String(36), db.ForeignKey('customers.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('appointments', lazy=True))

    def __init__(self, client_name: str, appointment_date: date, appointment_time: time, attendant_name: str, customer: Customer):
        self.id = str(uuid4())
        self.client_name = client_name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.attendant_name = attendant_name
        self.customer = customer
        self.customer_id = customer.id