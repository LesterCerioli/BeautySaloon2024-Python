import json
import datetime
import time

class CityService:
    def __init__(self, city_data, log_file="city_service_log.json"):
        """
        Initialize the CityService with the mock city data and log file path.
        :param city_data: A dictionary or list containing city information.
        :param log_file: Path to the log file to store logs.
        """
        self.city_data = city_data
        self.log_file = log_file

    def get_city_by_name(self, city_name):
        """
        Retrieve a city by its name.
        :param city_name: Name of the city to retrieve.
        :return: City information if found, else None.
        """
        # Simulate looking for the city by its name in the database
        for city in self.city_data:
            if city['name'].lower() == city_name.lower():
                return city
        return None

    def log_processing(self, city_name, status):
        """
        Log the city retrieval process details into a JSON file.
        :param city_name: Name of the city being processed.
        :param status: Status of the operation (success or failure).
        """
        log_entry = {
            "date": str(datetime.date.today()),
            "start_time": str(datetime.datetime.now()),
            "end_time": str(datetime.datetime.now()),
            "city_name": city_name,
            "status": status
        }

        
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

    def process_city_search(self, city_name):
        """
        Continuously search for a city by name until success.
        """
        is_success = False
        while not is_success:
            print(f"Starting city search for {city_name} at {datetime.datetime.now()}")
            city = self.get_city_by_name(city_name)

            if city:
                is_success = True
                self.log_processing(city_name, "success")
                print(f"City {city_name} found: {city}")
            else:
                self.log_processing(city_name, "failure")
                print(f"City {city_name} not found. Retrying...")

            # Retry after 3 seconds in case of failure
            if not is_success:
                time.sleep(3)

