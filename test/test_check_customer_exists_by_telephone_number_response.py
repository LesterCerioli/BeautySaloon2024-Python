

import unittest
from uuid import uuid4
from pydantic import ValidationError, BaseModel

# Importe a classe que você deseja testar
from application.handlers.customers.responses.check_customer_exists_by_telephone_number_response import CheckCustomerExistsByTelephoneNumberResponse


class TestCheckCustomerExistsByTelephoneNumberResponse(unittest.TestCase):
    def test_init_with_validation_errors(self):
        # Exemplo de um resultado de validação simulado
        validation_result = ValidationError(model=BaseModel, errors=[{'loc': ('exists',), 'msg': 'Example error', 'type': 'value_error'}])
        
        # Criação de uma instância de resposta para testar
        response = CheckCustomerExistsByTelephoneNumberResponse(request_id=uuid4(), exists=False, validation_result=validation_result)
        
        # Asserções para verificar se a inicialização ocorreu conforme o esperado
        self.assertEqual(response.exists, False)
        self.assertEqual(response.errors, ['Example error'])

    def test_init_with_false_validation(self):
        # Criação de uma instância de resposta para testar com falsa validação
        response = CheckCustomerExistsByTelephoneNumberResponse(request_id=uuid4(), exists=False, false_validation="Validation failed")
        
        # Asserções para verificar se a inicialização ocorreu conforme o esperado
        self.assertEqual(response.exists, False)
        self.assertEqual(response.errors, ["Validation failed"])

    def test_init_without_errors(self):
        # Criação de uma instância de resposta para testar sem erros
        response = CheckCustomerExistsByTelephoneNumberResponse(request_id=uuid4(), exists=True)
        
        # Asserções para verificar se a inicialização ocorreu conforme o esperado
        self.assertEqual(response.exists, True)
        self.assertEqual(response.errors, [])


if __name__ == '__main__':
    unittest.main()
