import random
import threading
import time

class Cnpj:
    def __init__(self, value: str):
        self.value = value

class Subscription:
    def __init__(self, cnpj: Cnpj, subscription_number: str):
        self.cnpj = cnpj
        self.subscription_number = subscription_number
        self._saloons = []
        self._lock = threading.Lock()

    @classmethod
    def new_subscription(cls, cnpj: Cnpj, subscription_number: str):
        return cls(cnpj, subscription_number)

    def add_saloon(self, saloon):
        with self._lock:
            self._saloons.append(saloon)

    def saloons(self):
        with self._lock:
            return list(self._saloons)  # Return a copy to ensure it's read-only

def generate_subscription_number() -> str:
    vowels = "AEIOU"
    numbers = "0123456789"

    
    random.seed(time.time())

    
    random_vowels = ''.join(random.choice(vowels) for _ in range(3))

    
    random_numbers = ''.join(random.choice(numbers) for _ in range(7))

    
    return random_vowels + random_numbers
