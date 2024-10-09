import json
import datetime
import threading
from typing import List


class SubscriptionService:
    def __init__(self, log_file="subscription_processing_log.json"):
        self.log_file = log_file  # Log file to store the processing details

    def log_processing(self, subscription_number: str, status: str, additional_info: str = None):
        """
        Log the subscription processing details into a JSON file.
        """
        log_entry = {
            "date": str(datetime.date.today()),
            "start_time": str(datetime.datetime.now()),
            "subscription_number": subscription_number,
            "status": status,
            "additional_info": additional_info,
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

    def create_subscription(self, cnpj_value: str, subscription_number: str = None) -> Subscription:
        """
        Create a new subscription with the provided CNPJ and optional subscription number.
        """
        if subscription_number is None:
            subscription_number = generate_subscription_number()

        cnpj = Cnpj(cnpj_value)
        subscription = Subscription.new_subscription(cnpj, subscription_number)

        self.log_processing(subscription_number, "created")
        print(f"Subscription created with number: {subscription_number}")

        return subscription

    def add_saloon_to_subscription(self, subscription: Subscription, saloon_name: str):
        """
        Add a saloon to a subscription.
        """
        try:
            subscription.add_saloon(saloon_name)
            self.log_processing(subscription.subscription_number, "saloon_added", f"Saloon {saloon_name} added")
            print(f"Saloon {saloon_name} added to subscription {subscription.subscription_number}.")
        except Exception as e:
            self.log_processing(subscription.subscription_number, "failure", str(e))
            print(f"Failed to add saloon to subscription {subscription.subscription_number}: {e}")

    def get_saloons_by_subscription(self, subscription: Subscription) -> List[str]:
        """
        Retrieve all saloons related to a subscription.
        """
        saloons = subscription.saloons()
        self.log_processing(subscription.subscription_number, "saloons_retrieved")
        print(f"Retrieved {len(saloons)} saloons for subscription {subscription.subscription_number}.")
        return saloons


