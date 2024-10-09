

class State:
    def __init__(self, state_name: str = None, uf: str = None):
        self.state_name = state_name
        self.uf = uf

    def set_state_name(self, name: str):
        self.state_name = name

    def set_uf(self, uf: str):
        self.uf = uf
