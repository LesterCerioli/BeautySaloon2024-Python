class City:
    def __init__(self, city_name: str = None):
        self.city_name = city_name
        self._states = []  # private field for states
        self.state = None  # primary state, like in your C# model

    @classmethod
    def new_city(cls, city_name: str):
        return cls(city_name)

    def add_state(self, state):
        self._states.append(state)

    def get_states(self):
        return self._states
