import json
import os
from datetime import datetime
from typing import List, Optional


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


class SaloonService:
    def __init__(self, log_file="saloon_log.json"):
        self.saloons: List[Saloon] = []
        self.log_file = log_file

    def add_saloon(self, saloon: Saloon):
        """Add a new saloon."""
        if self.get_saloon_by_cnpj(saloon.cnpj):
            raise Exception(f"Saloon with CNPJ {saloon.cnpj} already exists.")
        
        self.saloons.append(saloon)
        self.log_processing(saloon, "created")

    def update_saloon(self, cnpj: str, fantasy_name: Optional[str] = None, 
                      social_reason: Optional[str] = None, owner_name: Optional[str] = None,
                      telephone: Optional[str] = None, address: Optional[str] = None,
                      district: Optional[str] = None):
        """Update an existing saloon by CNPJ."""
        saloon = self.get_saloon_by_cnpj(cnpj)
        if not saloon:
            raise Exception(f"Saloon with CNPJ {cnpj} not found.")
        
        if fantasy_name:
            saloon.set_fantasy_name(fantasy_name)
        if social_reason:
            saloon.set_social_reason(social_reason)
        if owner_name:
            saloon.set_owner_name(owner_name)
        if telephone:
            saloon.set_telephone(telephone)
        if address:
            saloon.set_address(address)
        if district:
            saloon.set_district(district)

        self.log_processing(saloon, "updated")

    def get_saloon_by_cnpj(self, cnpj: str) -> Optional[Saloon]:
        """Retrieve a saloon by its CNPJ."""
        for saloon in self.saloons:
            if saloon.cnpj == cnpj:
                return saloon
        return None

    def get_all_saloons(self) -> List[Saloon]:
        """Get a list of all saloons."""
        return self.saloons

    def get_saloon_by_district(self, district: str) -> List[Saloon]:
        """
        Retrieve all saloons in a given district.
        """
        return [saloon for saloon in self.saloons if saloon.district == district]

    def get_saloon_by_fantasy_name(self, fantasy_name: str) -> List[Saloon]:
        """
        Retrieve all saloons with the given fantasy name.
        """
        return [saloon for saloon in self.saloons if saloon.fantasy_name == fantasy_name]

    def log_processing(self, saloon: Saloon, action: str):
        """
        Log the operation performed on a saloon (create/update).
        Logs the saloon information, action, and timestamps.
        """
        log_entry = {
            "date": str(datetime.now().date()),
            "start_time": str(datetime.now()),
            "saloon": {
                "fantasy_name": saloon.fantasy_name,
                "social_reason": saloon.social_reason,
                "cnpj": saloon.cnpj,
                "owner_name": saloon.owner_name,
                "telephone": saloon.telephone,
                "address": saloon.address,
                "district": saloon.district
            },
            "action": action,
            "status": "success",
            "end_time": str(datetime.now())
        }

        
        try:
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r+') as f:
                    data = json.load(f)
                    data.append(log_entry)
                    f.seek(0)
                    json.dump(data, f, indent=4)
            else:
                with open(self.log_file, 'w') as f:
                    json.dump([log_entry], f, indent=4)
        except Exception as e:
            print(f"Failed to log operation: {e}")

    def delete_saloon(self, cnpj: str):
        """
        Delete a saloon by its CNPJ.
        """
        saloon = self.get_saloon_by_cnpj(cnpj)
        if saloon:
            self.saloons.remove(saloon)
            self.log_processing(saloon, "deleted")
        else:
            raise Exception(f"Saloon with CNPJ {cnpj} not found.")



