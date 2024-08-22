
from domain.exceptions.applicationexception import ApplicationException


class NotFoundException(ApplicationException):
    def __init__(self, message: str):
        super().__init__(message=f"Not Found: {message}", title="Not Found")