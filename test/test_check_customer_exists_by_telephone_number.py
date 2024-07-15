

import unittest
from uuid import UUID
from application.handlers.customers.requests.check_customer_exists_by_telephone_number import CheckCustomerExistsByTelephoneNumber
from value_objects.telephone import Telephone


class TestCheckCustomerExistsByTelephoneNumber(unittest.TestCase):
    def test_init_with_telephone(self):
        telephone = Telephone(ddd='12', telephone_number='123456789')
        request = CheckCustomerExistsByTelephoneNumber(telephone=telephone)
        self.assertIsInstance(request.id, UUID)
        self.assertEqual(request.telephone, telephone)

    def test_init_without_telephone(self):
        request = CheckCustomerExistsByTelephoneNumber()
        self.assertIsInstance(request.id, UUID)
        self.assertIsNone(request.telephone)