from datetime import datetime
from domain.models.appointment import Appointment
from application import db  # Import the db instance from your application module

class AppointmentController:
    @staticmethod
    def create_appointment(data):
        if not data.get('date') or not data.get('appointment_hour'):
            raise ValueError("Missing required fields")
        
        new_appointment = Appointment(
            date=datetime.fromisoformat(data['date']),
            appointment_hour=datetime.fromisoformat(data['appointment_hour'])
        )
        db.session.add(new_appointment)
        db.session.commit()
        return new_appointment

    @staticmethod
    def get_appointment(appointment_id):
        appointment = Appointment.query.get(appointment_id)
        if appointment is None:
            raise ValueError("Appointment not found")
        return appointment

    @staticmethod
    def update_appointment(appointment_id, data):
        appointment = Appointment.query.get(appointment_id)
        if appointment is None:
            raise ValueError("Appointment not found")

        if 'date' in data:
            appointment.date = datetime.fromisoformat(data['date'])
        if 'appointment_hour' in data:
            appointment.appointment_hour = datetime.fromisoformat(data['appointment_hour'])

        db.session.commit()
        return appointment

    @staticmethod
    def delete_appointment(appointment_id):
        appointment = Appointment.query.get(appointment_id)
        if appointment is None:
            raise ValueError("Appointment not found")

        db.session.delete(appointment)
        db.session.commit()
