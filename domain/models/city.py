

class City:
    def __init__(self, city_name: str = None):
        self._city_name = city_name
        self._states = []

    @property
    def city_name(self):
        return self._city_name

    @property
    def state(self):
        if self._states:
            return self._states[0]  # Retorna o primeiro estado da lista, se existir
        return None

    @property
    def states(self):
        return self._states.copy()  # Retorna uma cópia da lista de estados como uma coleção somente leitura

    def add_state(self, state):
        self._states.append(state)

    def __repr__(self):
        return f"City(city_name={self.city_name}, state={self.state})"