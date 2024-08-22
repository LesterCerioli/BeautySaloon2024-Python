

from typing import Optional
from uuid import uuid4

from domain.models.attendant import Attendant


class CreateAttendantCommand:
    def __init__(self, id: Optional[str] = None):
        self.id: str = id or str(uuid4())
        self.attendant_name: Optional[str] = None

    def get_entity(self) -> Attendant:
        return Attendant(self.attendant_name)