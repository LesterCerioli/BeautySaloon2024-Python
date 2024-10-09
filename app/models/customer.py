
from valueobjects.telephone import Telephone

class Customer:
    def __init__(self, customer_name: str = None, email: str = None, telephone: Telephone = None):
        self.customer_name = customer_name
        self.email = email
        self.telephone = telephone  # Use Telephone value object here
    @classmethod
    def new_customer(cls, customer_name: str, email: str, telephone: Telephone):
        return cls(customer_name, email, telephone)

    def set_customer_name(self, customer_name: str):
        self.customer_name = customer_name

    def set_email(self, email: str):
        self.email = email

    def set_telephone(self, telephone: Telephone):
        self.telephone = telephone