

from dataclasses import field
from typing import Optional
from uuid import uuid4


class CustomerViewModel:
    id: str = field(default_factory=lambda: str(uuid4()), init=False)
    customer_name: Optional[str] = field(default=None, metadata={"display_name": "Nome do Cliente"})
    email: Optional[str] = field(default=None, metadata={"display_name": "Email"})
    telephone: Optional[str] = field(default=None, metadata={"display_name": "Número de Telefone"})

    def __post_init__(self):
        # Aqui você pode adicionar lógica adicional de inicialização, se necessário.
        pass