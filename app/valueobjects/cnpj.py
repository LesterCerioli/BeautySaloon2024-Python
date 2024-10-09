
import re

class Cnpj:
    def __init__(self, cnpj_number):
        if not self.is_valid(cnpj_number):
            raise ValueError("Invalid CNPJ number")
        self.cnpj_number = cnpj_number

    def get_cnpj_number(self):
        return self.cnpj_number

    def is_valid(self, cnpj_number):
        if not cnpj_number:
            return False
        cnpj_number = self.clean_cnpj(cnpj_number)
        if len(cnpj_number) != 14 or self.is_repeated_digits(cnpj_number) or not self.is_valid_checksum(cnpj_number):
            return False
        return True

    def clean_cnpj(self, cnpj_number):
        return re.sub(r'\D', '', cnpj_number)

    def is_repeated_digits(self, cnpj_number):
        return len(set(cnpj_number)) == 1

    def is_valid_checksum(self, cnpj_number):
        def calculate_digit(cnpj, multipliers):
            total = sum(int(digit) * multiplier for digit, multiplier in zip(cnpj, multipliers))
            remainder = total % 11
            return '0' if remainder < 2 else str(11 - remainder)

        cnpj = cnpj_number[:12]
        multipliers = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        digit1 = calculate_digit(cnpj, multipliers)
        cnpj += digit1
        multipliers = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        digit2 = calculate_digit(cnpj, multipliers)
        return cnpj_number[-2:] == digit1 + digit2

