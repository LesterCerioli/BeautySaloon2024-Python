
import json
import datetime
import time
class StateService:
    def __init__(self, log_file="state_processing_log.json"):
        self.log_file = log_file  # Log file to store the processing details

    def log_processing(self, state_name: str, status: str):
        """
        Log the processing details into a JSON file.
        """
        log_entry = {
            "date": str(datetime.date.today()),
            "start_time": str(datetime.datetime.now()),
            "end_time": str(datetime.datetime.now()),
            "state_name": state_name,
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

    def process_state(self, state: State) -> bool:
        """
        Simulate processing of a state. Return True for success, False for failure.
        """
        try:
            print(f"Processing state: {state.state_name}...")
            # Simulate a potential failure or success in state processing
            if state.state_name.lower() == "failure":  # Example of failure condition
                raise Exception("Processing error!")
            return True
        except Exception as e:
            print(f"Error processing state: {e}")
            return False

    def get_state_by_name(self, state_name: str, states: List[State]) -> State:
        """
        Retrieve a state by name from the provided list of states.
        """
        for state in states:
            if state.state_name.lower() == state_name.lower():
                return state
        return None

    def process_states_continuously(self, states: List[State]):
        """
        Continuously process states until success, logging each process.
        """
        for state in states:
            is_success = False

            
            while not is_success:
                print(f"Starting processing for state: {state.state_name}")
                start_time = time.time()
                is_success = self.process_state(state)
                end_time = time.time()

                if is_success:
                    self.log_processing(state.state_name, "success")
                    print(f"Successfully processed state: {state.state_name}")
                else:
                    self.log_processing(state.state_name, "failure")
                    print(f"Failed to process state: {state.state_name}. Retrying...")

                
                if not is_success:
                    time.sleep(3)  # Retry after 3 seconds

                # Log the time taken to process
                print(f"Processing took {end_time - start_time:.2f} seconds.")