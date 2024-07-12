

from typing import Optional
from uuid import UUID


class CheckCustomerExistsByTelephoneNumber(BaseModel) # type: ignore:
    id: UUID
    telephone_number = Optional[str]
    
    def __init__(self, telephone_number: Optional[str] = None):
        
    
