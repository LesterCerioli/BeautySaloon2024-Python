from typing import Optional
from uuid import uuid4
from models import Address, Cnpj, District, Telephone


class Saloon:
    def __init__(
        self, 
        fantasy_name: Optional[str], 
        social_reason: Optional[str], 
        cnpj: Cnpj, 
        district: District, 
        owner_name: Optional[str], 
        telephone: Telephone, 
        address: Address,
        value: Optional[object] = None
    ):
        self.id = uuid4()  # ID gerado automaticamente
        self.fantasy_name = fantasy_name
        self.social_reason = social_reason
        self.cnpj = cnpj
        self.owner_name = owner_name
        self.telephone = telephone
        self.address = address
        self.district = district
        self.value = value

    def __repr__(self):
        return (f"Saloon(id={self.id}, fantasy_name={self.fantasy_name}, social_reason={self.social_reason}, "
                f"cnpj={self.cnpj}, owner_name={self.owner_name}, telephone={self.telephone}, "
                f"address={self.address}, district={self.district}, value={self.value})")

    def __eq__(self, other):
        if not isinstance(other, Saloon):
            return False
        return (self.fantasy_name == other.fantasy_name and
                self.social_reason == other.social_reason and
                self.cnpj == other.cnpj and
                self.owner_name == other.owner_name and
                self.telephone == other.telephone and
                self.address == other.address and
                self.district == other.district and
                self.value == other.value)

    def __hash__(self):
        return hash((self.fantasy_name, self.social_reason, self.cnpj, self.owner_name,
                     self.telephone, self.address, self.district, self.value))

    def get_equality_components(self):
        return [self.fantasy_name, self.social_reason, self.cnpj, self.owner_name,
                self.telephone, self.address, self.district, self.value]