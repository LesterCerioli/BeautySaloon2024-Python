

from collections import UserList
from typing import Any, Iterable, List, TypeVar

TRequest = TypeVar('TRequest', bound=BaseModel) # type: ignore
TResponse = TypeVar('TResponse', bound='Response')

class ReadOnlyCollection(UserList):
    def __setitem__(self, i, item):
        raise TypeError("Read-only collection")
    
    def __delitem__(self, i):
        raise TypeError("Read-only collection")
    
    def append(self, item):
        raise TypeError("Read-only collection")
    
    def insert(self, i, item):
        raise TypeError("Read-only collection")
    
    def pop(self, i=-1):
        raise TypeError("Read-only collection")
    
    def remove(self, item):
        raise TypeError("Read-only collection")
    
    def clear(self):
        raise TypeError("Read-only collection")

class Response:
    def __init__(self, result: Any = None):
        self._message: List[str]  = []
        self.errors: Iterable[str] = ReadOnlyCollection(self._messages) # type: ignore
        self.result: Any = result
        
    def add_error(self, message: str) -> 'Response':
        self._messages.append(message)
        return self
    
response = Response()
response.add_error("An error occurred")
print(list(response.errors))  # ['An error occurred']
print(response.result)        # None

response_with_result = Response(result="Success")
print(response_with_result.result)  # 'Success'