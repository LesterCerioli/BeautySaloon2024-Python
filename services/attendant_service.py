import json
import time
from datetime import datetime
import random


class Attendant:
    def __init__(self, attendant_name: str = None):
        self.attendant_name = attendant_name

    @classmethod
    def new_attendant(cls, attendant_name: str):
        return cls(attendant_name)


class AttendantService:
    def __init__(self, log_file="attendant_log.json"):
        self.attendants = []  # List to store attendants
        self.log_file = log_file

    def add_attendant(self, attendant: Attendant):
        """Add a new attendant."""
        self.attendants.append(attendant)
    
    def assign_appointments(self, appointment):
        """
        Try to assign the appointment to an available attendant.
        Retry in case of failure.
        """
        is_success = False
        while not is_success:
            available_attendant = self.get_available_attendant()
            if available_attendant:
                # Attempt to assign the appointment to the attendant
                is_success = self.assign_to_attendant(appointment, available_attendant)

                # Log the result of the assignment
                if is_success:
                    self.log_processing(available_attendant, "success")
                    print(f"Successfully assigned appointment to {available_attendant.attendant_name}")
                else:
                    self.log_processing(available_attendant, "failure")
                    print(f"Failed to assign appointment to {available_attendant.attendant_name}. Retrying in 3 seconds...")
                
                if not is_success:
                    time.sleep(3)  # Retry after 3 seconds
            else:
                print("No available attendants. Waiting for 3 seconds...")
                time.sleep(3)

    def assign_to_attendant(self, appointment, attendant):
        """
        Simulate the assignment of an appointment to an attendant.
        If the process fails, return False.
        """
        try:
            
            print(f"Assigning {appointment['customer_name']} to {attendant.attendant_name}...")
            if random.choice([True, False]):  # Randomize success/failure for simulation
                return True
            else:
                raise Exception("Random failure during assignment.")
        except Exception as e:
            print(f"Error during assignment: {e}")
            return False

    def get_available_attendant(self):
        """Fetch an available attendant (simulated)."""
        if self.attendants:
            return random.choice(self.attendants)  # Randomly pick an available attendant for this example
        return None

    def log_processing(self, attendant, status):
        """
        Log the assignment process.
        Logs the attendant name, processing time, and the status (success/failure).
        """
        log_entry = {
            "date": str(datetime.now().date()),
            "start_time": str(datetime.now()),
            "end_time": str(datetime.now()),
            "attendant_name": attendant.attendant_name,
            "status": status,
        }

        
        try:
            with open(self.log_file, 'r+') as f:
                data = json.load(f)
                data.append(log_entry)
                f.seek(0)
                json.dump(data, f, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.log_file, 'w') as f:
                json.dump([log_entry], f, indent=4)

    def process_attendants(self, appointments):
        """
        Continuously process appointments and try to assign them to available attendants.
        """
        for appointment in appointments:
            print(f"Processing appointment for {appointment['customer_name']}")
            self.assign_appointments(appointment)


