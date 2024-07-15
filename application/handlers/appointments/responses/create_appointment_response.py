

from application.core.response import Response


class CreateAppointmentResponse(Response):
    def __init__(self, request_id: UUID, validator: IValidator, data: dict, false_validation: str = None): # type: ignore
        super().__init__()
        self.request_id = request_id
        
        errors = validator.validate(data)
        for error in errors:
            self.add_error(error)
                
        if false_validation:
            self.add_error(false_validation)