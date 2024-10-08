import re

class Telephone:
    def __init__(self, telephone_number: str, telephone_region: str):
        self.telephone_number = telephone_number
        self.telephone_region = telephone_region

    @classmethod
    def new_telephone(cls, telephone_number: str, telephone_region: str):
        if not cls.validate_telephone(telephone_number):
            raise ValueError("Invalid telephone number")
        return cls(telephone_number, telephone_region)

    @staticmethod
    def validate_telephone(telephone: str) -> bool:
        # Trims whitespace
        shorten_num = telephone.strip()

        
        shorten_num = re.sub(r'[^0-9a-zA-Z]+', '', shorten_num)

        
        if len(shorten_num) == 13:
            print("The telephone number is valid")
            return True
        print("The telephone number is invalid")
        return False
