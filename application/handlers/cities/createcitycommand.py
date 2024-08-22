

from typing import Optional
from uuid import uuid4

from domain.models.city import City


class CreateCityCommand:
    def __init__(self):
        self.id: str = str(uuid4())
        self.city_name: Optional[str] = None

    def get_entity(self) -> City:
        return City(
            self.city_name
        )