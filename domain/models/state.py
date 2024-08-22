from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4

@dataclass
class State:
    id: str = field(default_factory=lambda: str(uuid4()))  # ID gerado automaticamente
    state_name: Optional[str] = None
    uf: Optional[str] = None

    def __post_init__(self):
        if self.state_name is None:
            raise ValueError("State name cannot be empty")
        if self.uf is None:
            raise ValueError("UF cannot be empty")

    def __repr__(self):
        return (f"State(id={self.id}, state_name={self.state_name}, uf={self.uf})")

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return (self.state_name == other.state_name and
                self.uf == other.uf)

    def __hash__(self):
        return hash((self.state_name, self.uf))

    def get_equality_components(self):
        return [self.state_name, self.uf]
