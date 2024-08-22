

from uuid import UUID
from xml.dom import ValidationErr
from application.core.response import Response


class CreateStateResponse(Response):
    def __init__(self, request_id: UUID, result: ValidationErr = None, validation_failure: str = None):
        super().__init__()
        self.request_id = request_id

        # Adiciona erros da validação, se existirem
        if result:
            for error in result.errors():
                self.add_error(error['msg'])

        # Adiciona uma falha de validação, se fornecida
        if validation_failure:
            self.add_error(validation_failure)