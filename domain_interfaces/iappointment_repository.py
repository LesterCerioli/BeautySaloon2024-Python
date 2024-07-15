from models.appointment import Appointment
from sqlalchemy.orm import sessionmaker



class IAppointmentRepository:
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_appointment(self, customer_name, appointment_date, appointment_time, attendant_name, customer):
        appointment = Appointment(
            customer_name=customer_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            attendant_name=attendant_name,
            customer=customer
        )
        self.session.add(appointment)
        self.session.commit()
        return appointment
    

    def update_appointment(self, appointment_id, customer_name=None, appointment_date=None, appointment_time=None, attendant_name=None, customer=None):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            if customer_name:
                appointment.client_name = customer_name
            if appointment_date:
                appointment.appointment_date = appointment_date
            if appointment_time:
                appointment.appointment_time = appointment_time
            if attendant_name:
                appointment.attendant_name = attendant_name
            if customer:
                appointment.customer = customer
                appointment.customer_id = customer.id
            self.session.commit()
        return appointment

    def delete_appointment(self, appointment_id):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            self.session.delete(appointment)
            self.session.commit()
        return appointment
