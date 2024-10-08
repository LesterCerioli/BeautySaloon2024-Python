
class Address:
    def __init__(self, avenue_or_street, number):
        self.avenue_or_street = avenue_or_street
        self.number = number
        
def new_address(avenue_or_street, number):
    return Address(avenue_or_street, number)