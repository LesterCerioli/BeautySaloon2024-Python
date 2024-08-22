import uuid
from typing import Optional

class Attendant:
    def __init__(self, attendant_name: Optional[str] = None):
        self.id = uuid.uuid4()  # Geração automática do GUID
        self.attendant_name = attendant_name

    def __repr__(self):
        return f"Attendant(id={self.id}, attendant_name={self.attendant_name})"


attendant = Attendant("John Doe")
print(attendant)  # Exemplo de saída: Attendant(id=<algum_guid>, attendant_name='John Doe')
