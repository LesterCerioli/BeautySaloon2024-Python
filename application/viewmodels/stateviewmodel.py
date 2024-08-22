

from dataclasses import field
from typing import Optional
from uuid import uuid4


class StateViewModel:   
    id: str = field(default_factory=lambda: str(uuid4()), init=False)
    state_name: Optional[str] = field(default=None, metadata={"display_name": "Nome de Estado"})
    uf: Optional[str] = field(default=None, metadata={"display_name": "UF"})

    def __post_init__(self):
        # Qualquer lógica adicional de inicialização, se necessário
        pass