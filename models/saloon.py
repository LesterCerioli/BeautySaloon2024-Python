

class Saloon:
    def __init__(self, fantasy_name: str = None, social_reason: str = None, cnpj: str = None, 
                owner_name: str = None, telephone: str = None, address: str = None, district: str = None):
        self.fantasy_name = fantasy_name
        self.social_reason = social_reason
        self.cnpj = cnpj
        self.owner_name = owner_name
        self.telephone = telephone
        self.address = address
        self.district = district
        
    @classmethod
    def new_saloon(cls, fantasy_name: str, social_reason: str, cnpj: str, owner_name: str,
                   telephone: str, address: str, district: str):
        return cls(fantasy_name, social_reason, cnpj, owner_name, telephone, address, district)

    def set_fantasy_name(self, fantasy_name: str):
        self.fantasy_name = fantasy_name

    def set_social_reason(self, social_reason: str):
        self.social_reason = social_reason

    def set_cnpj(self, cnpj: str):
        self.cnpj = cnpj

    def set_owner_name(self, owner_name: str):
        self.owner_name = owner_name

    def set_telephone(self, telephone: str):
        self.telephone = telephone

    def set_address(self, address: str):
        self.address = address

    def set_district(self, district: str):
        self.district = district