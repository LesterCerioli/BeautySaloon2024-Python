
import logging
from typing import Optional
from pydantic import BaseModel, ValidationError
from uuid import uuid4
import json
from datetime import date, time

class CheckAppointmentsByAppointmentDateRequest(BaseModel):
    id: str
    appointment_date: date
    appointment_time: time

    def __init__(self, appointment_date: date, appointment_time: time):
        super().__init__(id=str(uuid4()), appointment_date=appointment_date, appointment_time=appointment_time)

class CheckAppointmentsByAppointmentDateResponse(BaseModel):
    id: str
    exists: bool
    message: Optional[str] = None
    validation_result: Optional[dict] = None

class CheckAppointmentsByAppointmentDateRequestValidation:
    @staticmethod
    def validate(request: CheckAppointmentsByAppointmentDateRequest):
        errors = []
        if not request.appointment_date:
            errors.append("Appointment date is required.")
        if not request.appointment_time:
            errors.append("Appointment time is required.")
        return errors

class IAppointmentRepository:
    async def get_by_appointment_date_and_time(self, appointment_date: date, appointment_time: time) -> Optional[dict]:
        # Placeholder for the actual implementation
        pass

class CheckAppointmentsExistsByAppointmentDateHandler:
    def __init__(self, appointment_repository: IAppointmentRepository):
        self._appointment_repository = appointment_repository
        self._logger = logging.getLogger(__name__)

    async def handle(self, request: CheckAppointmentsByAppointmentDateRequest) -> CheckAppointmentsByAppointmentDateResponse:
        self._logger.info(f"CheckAppointmentsByAppointmentDateRequest: {json.dumps(request.dict())}")

        validation_result = CheckAppointmentsByAppointmentDateRequestValidation.validate(request)
        if not validation_result:
            try:
                appointment = await self._appointment_repository.get_by_appointment_date_and_time(request.appointment_date, request.appointment_time)

                if appointment:
                    return CheckAppointmentsByAppointmentDateResponse(id=request.id, exists=True, validation_result=validation_result)
            except Exception as ex:
                self._logger.critical(ex, exc_info=True)
                return CheckAppointmentsByAppointmentDateResponse(id=request.id, exists=False, message="Failed to process the request.")
        
        return CheckAppointmentsByAppointmentDateResponse(id=request.id, exists=False, validation_result=validation_result)


async def main():
    handler = CheckAppointmentsExistsByAppointmentDateHandler(IAppointmentRepository())
    request = CheckAppointmentsByAppointmentDateRequest(appointment_date=date(2024, 7, 15), appointment_time=time(14, 30))
    response = await handler.handle(request)
    print(response)

import asyncio
asyncio.run(main())
