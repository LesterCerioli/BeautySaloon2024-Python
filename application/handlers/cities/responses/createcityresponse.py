

from typing import Optional
from uuid import UUID
from xml.dom import ValidationErr
from application.core.response import Response


class CreateCityResponse(Response):
    request_id: UUID

    def __init__(self, request_id: UUID, result: Optional[ValidationErr] = None, validation_failure: Optional[str] = None):
        super().__init__()
        self.request_id = request_id
        
        if result:
            for error in result.errors():
                self.add_error(error['msg'])
                
        if validation_failure:
            self.add_error(validation_failure)


try:
    # Simulating a validation result
    class MockValidationResult:
        def errors(self):
            return [{'msg': 'Error 1'}, {'msg': 'Error 2'}]
    
    result = MockValidationResult()
    response = CreateCityResponse(request_id=UUID('12345678123456781234567812345678'), result=result)
    print(response)
except ValidationErr as e:
    print(f"Validation Error: {e}")