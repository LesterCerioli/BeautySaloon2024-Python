

from models.appointment import Appointment
from domain_interfaces.iappointment_repository import IAppointmentRepository
from sqlalchemy.orm import sessionmaker


class AppointmentRepository(IAppointmentRepository):
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_by_appointment_date(self, appointment_date):
        appointments = self.session.query(Appointment).filter_by(appointment_date=appointment_date).all()
        return appointments

    def get_by_appointment_time(self, appointment_time):
        appointments = self.session.query(Appointment).filter_by(appointment_time=appointment_time).all()
        return appointments

    def create_appointment(self, customer_name, appointment_date, appointment_time, attendant_name, customer):
        appointment = Appointment(
            client_name=customer_name,
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

    def get_appointment_by_id(self, appointment_id):
        appointment = self.session.query(Appointment).filter_by(id=appointment_id).first()
        return appointment
