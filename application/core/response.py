from collections import UserList
from typing import Any, Iterable, List, TypeVar

TRequest = TypeVar('TRequest', bound='BaseModel')  # Assuming BaseModel is defined elsewhere
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
        self._message: List[str]  = []  # Corrected variable name to _message
        self.errors: Iterable[str] = ReadOnlyCollection(self._message)  # Corrected reference to _message
        self.result: Any = result
        
    def add_error(self, message: str) -> 'Response':
        self._message.append(message)  # Corrected variable name to _message
        return self
    
response = Response()
response.add_error("An error occurred")
print(list(response.errors))  # Output: ['An error occurred']
print(response.result)        # Output: None

response_with_result = Response(result="Success")
print(response_with_result.result)  # Output: 'Success'
