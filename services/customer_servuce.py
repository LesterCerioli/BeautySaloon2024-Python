import datetime
from models.customer import Customer


class CustomerService:
    def __init__(self, log_file="customer_processing_log.json"):  # Fixed the method name __init__
        self.log_file = log_file

    def process_customer(self, customer: Customer):
        """
        Processes the customer's registration. Simulates a potential processing failure.
        Returns True for success and False for failure.
        """
        try:
            print(f"Processing customer {customer.customer_name}...")
            # Simulated success
            return True
        except Exception as e:
            print(f"Error processing customer: {e}")
            return False

    def log_processing(self, customer: Customer, status: str):
        """
        Logs the processing in a JSON file.
        """
        log_entry = {
            "date": str(datetime.date.today()),
            "start_time": str(datetime.datetime.now()),
            "end_time": str(datetime.datetime.now()),
            "customer_name": customer.customer_name,
            "status": status
        }
        

    def process_customers_continuously(self, customers):
        """
        Continuously processes customers until the status is "success".
        """
        for customer in customers:
            is_success = False

            while not is_success:
                print(f"Starting processing for {customer.customer_name}...")
                is_success = self.process_customer(customer)

                if is_success:
                    self.log_processing(customer, "success")
                    print(f"Successfully processed customer {customer.customer_name}")
                else:
                    self.log_processing(customer, "failure")
                    print(f"Failed to process customer {customer.customer_name}. Retrying...")
