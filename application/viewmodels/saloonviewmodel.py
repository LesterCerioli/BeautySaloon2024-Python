

from dataclasses import field
from typing import Optional
from uuid import uuid4

from value_objects.cnpj import Cnpj


class SaloonViewModel:
    id: str = field(default_factory=lambda: str(uuid4()), init=False)
    fantasy_name: Optional[str] = field(default=None, metadata={"display_name": "Nome Fantasia"})
    social_reason: Optional[str] = field(default=None, metadata={"display_name": "Razão Social"})
    cnpj: Optional[Cnpj] = field(default=None, metadata={"display_name": "CNPJ"})
    owner_name: Optional[str] = field(default=None, metadata={"display_name": "Proprietário do negócio"})
    telephone: Optional[str] = field(default=None, metadata={"display_name": "Número de Telefone"})
    address: Optional[str] = field(default=None, metadata={"display_name": "Endereço Completo"})
    district: Optional[str] = field(default=None, metadata={"display_name": "Bairro"})

    def __post_init__(self):
        # Lógica adicional de inicialização, se necessário
        pass