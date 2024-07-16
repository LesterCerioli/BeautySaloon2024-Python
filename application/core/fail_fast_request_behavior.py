

from typing import Any, TypeVar, Generic, List, Callable, Awaitable, Type
from pydantic import BaseModel, ValidationError, validator # type: ignore
from collections.abc import Iterable
from collections import UserList
from asyncio import iscoroutinefunction

TRequest = TypeVar('TRequest', bound=BaseModel)
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
        self._messages: List[str] = []
        self.errors: Iterable[str] = ReadOnlyCollection(self._messages)
        self.result: Any = result

    def add_error(self, message: str) -> 'Response':
        self._messages.append(message)
        return self

class FailFastRequestBehavior(Generic[TRequest, TResponse]):
    def __init__(self, validators: List[Callable[[TRequest], Awaitable[None]]]):
        self._validators = validators

    async def errors(self, failures: List[str]) -> TResponse:
        response = Response()
        for failure in failures:
            response.add_error(failure)
        return response

    async def handle(self, request: TRequest, next: Callable[[], Awaitable[TResponse]]) -> TResponse:
        failures = []
        for validate in self._validators:
            try:
                if iscoroutinefunction(validate):
                    await validate(request)
                else:
                    validate(request)
            except ValidationError as e:
                failures.extend([err['msg'] for err in e.errors()])

        if failures:
            return await self.errors(failures)
        return await next()


class GenericRequest(BaseModel):
    name: str

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Name must not be empty')
        return v

async def example_handler() -> Response:
    return Response(result="Success")

# Validator function
async def validate_request(request: GenericRequest):
    request.validate()

# Create behavior with validators
behavior = FailFastRequestBehavior[GenericRequest, Response](validators=[validate_request])

# Generalized main function
async def main(request_data: dict, request_type: Type[TRequest]):
    request = request_type(**request_data)
    response = await behavior.handle(request, example_handler)
    print(list(response.errors))  # Should be empty if no validation errors
    print(response.result)        # 'Success'

import asyncio

# Example usage of the generalized main function
request_data = {"name": "John Doe"}
asyncio.run(main(request_data, GenericRequest))

