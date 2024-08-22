
from domain.exceptions.applicationexception import ApplicationException


class BadRequestException(ApplicationException):
    def __init__(self, message: str):
        super().__init__(message=f"Bad Request: {message}", title="Bad Request")