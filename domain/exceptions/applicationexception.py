

class ApplicationException(Exception):
    def __init__(self, message: str = None, title: str = None):
        super().__init__(message)
        self.title = title

    def __str__(self):
        if self.title:
            return f"{self.title}: {self.args[0]}"
        return super().__str__()