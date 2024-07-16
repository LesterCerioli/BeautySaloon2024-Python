

from typing import Optional
from application.core.response import Response


class CheckAppointmentsByAppointmentDateResponse(Response):
    id: str
    exists: bool
    message: Optional[str] = None
    validation_result: Optional[dict] = None