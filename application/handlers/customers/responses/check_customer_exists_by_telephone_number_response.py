

from dataclasses import Field
from typing import List, Optional
from uuid import UUID
from application.core.response import Response


class CheckCustomerExistsByTelephoneNumberResponse(Response, BaseModel): # type: ignore
    request_id: UUID
    exists: bool
    errors: List[str] = Field(default_factory=list)
    
    def __init__(self, request_id: UUID, exists: bool, validation_result: Optional[ValidationError] = None, false_validation: Optional[str] = None): # type: ignore
        super().__init__()
        self.request_id = request_id
        self.exists = exists

        if validation_result:
            for item in validation_result.errors():
                self.add_error(item['msg'])
        elif false_validation:
            self.add_error(false_validation)

    class Config:
        arbitrary_types_allowed = True