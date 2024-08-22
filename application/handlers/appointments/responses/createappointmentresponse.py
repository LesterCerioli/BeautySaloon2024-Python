

from typing import Optional
from uuid import UUID
from xml.dom import ValidationErr
from application.core.response import Response


class CreateAppointmentResponse(Response):
    request_id: UUID

    def __init__(self, request_id: UUID, result: Optional[ValidationErr] = None, validation_failure: Optional[str] = None):
        super().__init__()
        self.request_id = request_id
        
        if result:
            # Adiciona erros de validação à lista de erros
            for error in result.errors():
                self.add_error(error['msg'])
                
        if validation_failure:
            # Adiciona mensagem de falha de validação à lista de erros
            self.add_error(validation_failure)