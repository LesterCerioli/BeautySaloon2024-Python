import sys
import os
import unittest
from datetime import date, time


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain_interfaces.iappointment_repository import MockAppointmentRepository

class TestIAppointmentRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MockAppointmentRepository()

    def test_get_id(self):
        self.assertEqual(self.repo.get_id(), "1")

    def test_get_set_client_name(self):
        self.repo.set_client_name("John Doe")
        self.assertEqual(self.repo.get_client_name(), "John Doe")

    def test_get_set_appointment_date(self):
        new_date = date(2024, 1, 1)
        self.repo.set_appointment_date(new_date)
        self.assertEqual(self.repo.get_appointment_date(), new_date)

    def test_get_set_appointment_time(self):
        new_time = time(14, 30)
        self.repo.set_appointment_time(new_time)
        self.assertEqual(self.repo.get_appointment_time(), new_time)

    def test_get_set_attendant_name(self):
        self.repo.set_attendant_name("Jane Smith")
        self.assertEqual(self.repo.get_attendant_name(), "Jane Smith")

    def test_get_customer_id(self):
        self.assertEqual(self.repo.get_customer_id(), "123")

if __name__ == '__main__':
    unittest.main()
