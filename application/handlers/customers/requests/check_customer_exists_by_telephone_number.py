

from typing import Optional
from uuid import UUID

from value_objects.telephone import Telephone


class CheckCustomerExistsByTelephoneNumber(BaseModel) # type: ignore # type: ignore:
    id: UUID
    telephone: Optional[Telephone] = None
    
    def __init__(self, telephone: Optional[Telephone] = None):
        super().__init__(telephone=telephone)
        
    
