

from datetime import date

from pydantic import ValidationError
from application.handlers.appointments.create_appointment_command import CreateAppointmentCommand


class CreateAppointmentCommandValidation:
    @staticmethod
    def validate(command: CreateAppointmentCommand):
        errors = []
        
        if not command.customer_name:
            errors.append("O campo nome do cliente é obrigatório.")
        elif len(command.customer_name) > 80:
            errors.append("O campo nome do cliente deve ter no máximo 80 caracteres.")

        
        if command.appointment_date is None:
            errors.append("Informe a data de agendamento do atendimento.")
        elif command.appointment_date < date.today():
            errors.append("A data do agendamento não pode ser anterior a data de hoje.")

        
        if command.appointment_time is None:
            errors.append("O campo hora de atendimento é obrigatório.")

           
        
        if errors:
            raise ValidationError(errors)