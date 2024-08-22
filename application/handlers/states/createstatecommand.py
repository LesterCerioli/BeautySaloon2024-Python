

from sre_parse import State
from typing import Optional
from uuid import uuid4


class CreateStateCommand:
    def __init__(self):
        self.id: str = str(uuid4())
        self.state_name: Optional[str] = None
        self.uf: Optional[str] = None

    def get_entity(self) -> State:
        return State(
            self.state_name,
            self.uf
        )