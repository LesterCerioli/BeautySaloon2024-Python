

import datetime


class Appoitnment:
    def __init_(self, date: datetime = None, appoitnment_hour: datetime = None, customer = None):
        self.date = date
        self.appointment_hour = appoitnment_hour
        self.attendants = []  
        self.customer = customer  
    @classmethod
    def new_appointment(cls, date: datetime, appointment_hour: datetime, customer):
        return cls(date, appointment_hour, customer)

    def add_attendant(self, attendant):
        self.attendants.append(attendant)

    def get_attendants(self):
        return self.attendants
class Attendant:
    def __init__(self, attendant_name: str):
        self.attendant_name = attendant_name

    def __repr__(self):
        return f"Attendant(Name: {self.attendant_name})"


class Customer:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name

    def __repr__(self):
        return f"Customer(Name: {self.customer_name})"
    