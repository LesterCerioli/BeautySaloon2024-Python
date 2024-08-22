from domain.exceptions.notFoundException import NotFoundException


class UserNotFoundException(NotFoundException):
    def __init__(self, user_id: int):
        message = f"The user with the identifier {user_id} was not found."
        super().__init__(message)