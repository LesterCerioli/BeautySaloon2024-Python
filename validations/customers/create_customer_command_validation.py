

from pydantic import ValidationError
from application.handlers.customers.crete_customer_command import CreateCustomerCommand


class CreateCustomerCommandValidation:
    @staticmethod
    def validate(command: CreateCustomerCommand):
        errors = []
        
        if not command.customer_name:
            errors.append("O campo nome do cliente é obrigatório.")
        elif len(command.customer_name) > 80:
            errors.append("O campo nome do cliente deve ter no máximo 80 caracteres.")
            
        if not command.address_email:
            errors.append("O campo endereço de email é de preenchimento obrigatório..")
        elif len(command.address_email) > 20:
            errors.append("O campo endereço de email deve possuir na máximo 20 caractere.")
            
        if not command.telephone_number:
            errors.append("O número do telefone deve ser informado.")
        elif len(command.telephone_number) > 11:
            errors.append("O número de telefone deve possuir no máximo 12 algarismos.")
            
        if errors:
            raise ValidationError(errors)