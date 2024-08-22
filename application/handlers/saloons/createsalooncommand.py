

from typing import Optional
from uuid import uuid4

from domain.models.saloon import Saloon
from value_objects.address import Address
from value_objects.cnpj import Cnpj
from value_objects.district import District
from value_objects.telephone import Telephone


class CreateSaloonCommand:
    def __init__(self):
        self.id: str = str(uuid4())
        self.fantasy_name: Optional[str] = None
        self.cnpj: Optional[str] = None
        self.social_reason: Optional[str] = None  # Fixed spelling from SocialReason
        self.owner_name: Optional[str] = None
        self.telephone: Optional[str] = None
        self.address: Optional[str] = None
        self.district: Optional[str] = None

    def get_entity(self) -> Saloon:
        return Saloon(
            self.fantasy_name,
            self.social_reason,
            Cnpj(self.cnpj),
            self.owner_name,
            Telephone(self.telephone),
            Address(self.address),
            District(self.district),
            None  # Placeholder for potential additional fields
        )