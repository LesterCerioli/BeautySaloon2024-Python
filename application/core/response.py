

from typing import Any, Iterable, List


class Response:
    def __init__(self, result: Any = None):
        self._messages: List[str] = []
        self.errors: Iterable[str] = self._messages
        self.result: Any = result

    def add_error(self, message: str) -> "Response":
        self._messages.append(message)
        return self