
from datetime import date
import json
import time
from typing import Optional
from flask import logging
from pydantic import BaseModel, ValidationError
from sqlalchemy import UUID

from application.handlers.appointments.create_appointment_command import CreateAppointmentCommand
from application.handlers.appointments.responses.create_appointment_response import CreateAppointmentResponse
from domain_interfaces.iappointment_repository import IAppointmentRepository
from infrastructure.repositories import appointment_repository
from validations.appointemnts.create_appointment_command_validation import CreateAppointmentCommandValidation


class CreateAppointmentHandler:
    def __init__(self, address_repository: IAppointmentRepository, logger: logging.Logger):
        self._appointment_repository = appointment_repository
        self._logger = logger
        
    async def handle(self, command: CreateAppointmentCommand) -> CreateAppointmentResponse:
        self._logger.info(f"CreateAppointemntCommand: {json.dumps(command.dict())}")
        validation_result = CreateAppointmentCommandValidation().validate(command)

        if not validation_result.errors():
            try:
                address_address_line = await self._appointemnt_repository.get_by_address_line(command.address_line1)
                address_contact_name = await self._appointemnt_repository.get_by_contact_name(command.contact_name)

                if address_contact_name and address_address_line:
                    return CreateAppointmentResponse(command.id, message="Address already registered!")

                await self._address_repository.add(command.get_entity())
                return CreateAppointmentResponse(command.id, validation_result=validation_result)
            except Exception as ex:
                self._logger.critical(ex, exc_info=True)
                return CreateAppointmentResponse(command.id, message="It's not possible to process your solicitation.")

        return CreateAppointmentResponse(command.id, validation_result=validation_result)
    
    