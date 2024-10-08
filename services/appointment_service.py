import datetime
import time
import json  # Missing import

class AppointmentService:
    def __init__(self, log_file="appointment_log.json"):
        self.log_file = log_file

    def process_appointment(self, appointment):
        """
        Process the appointment. Simulate a possible failure in processing.
        Return True for success and False for failure.
        """
        try:
            # Simulating appointment processing (replace with real logic)
            print(f"Processing appointment for {appointment.customer.customer_name}...")
            # Simulating possible failure
            if random.choice([True, False]):
                raise Exception("Simulated error in appointment processing.")
            return True
        except Exception as e:
            print(f"Error processing appointment: {e}")
            return False

    def log_processing(self, appointment, status):
        """
        Log the appointment processing details into a JSON file.
        """
        log_entry = {
            "date": str(datetime.date.today()),
            "start_time": str(datetime.datetime.now()),
            "end_time": str(datetime.datetime.now()),
            "customer_name": appointment.customer.customer_name,
            "status": status
        }

        # Append log entry to the JSON file
        try:
            with open(self.log_file, 'r+') as f:
                data = json.load(f)
                data.append(log_entry)
                f.seek(0)
                json.dump(data, f, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file not found or empty, create and write the log
            with open(self.log_file, 'w') as f:
                json.dump([log_entry], f, indent=4)

    def process_appointments_continuously(self, appointments):
        """
        Continuously process appointments until success.
        If any failure happens, retry the process at intervals of 3 seconds.
        """
        for appointment in appointments:
            is_success = False

            # Retry the appointment processing until success
            while not is_success:
                print(f"Starting processing for {appointment.customer.customer_name}")
                is_success = self.process_appointment(appointment)

                if is_success:
                    self.log_processing(appointment, "success")
                    print(f"Successfully processed appointment for {appointment.customer.customer_name}")
                else:
                    self.log_processing(appointment, "failure")
                    print(f"Failed to process appointment for {appointment.customer.customer_name}. Retrying...")

                # Wait before retrying, after failure, it will retry every 3 seconds
                if not is_success:
                    time.sleep(3)  # Retry after 3 seconds


