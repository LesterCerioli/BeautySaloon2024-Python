

class Attendant:
    def __init_(self, attendant_name: str = NotImplemented):
        self.attendant_name = attendant_name
    @classmethod
    def new_attendant(cls, attendant_name: str):
        return cls(attendant_name)
    

