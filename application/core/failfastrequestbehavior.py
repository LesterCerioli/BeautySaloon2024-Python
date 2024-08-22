from typing import Generic, TypeVar, List, Callable, Any, Awaitable

from asyncio import iscoroutinefunction
from typing import Awaitable, Callable, Generic, List
from urllib.request import Request
from xml.dom import ValidationErr

from application.core.response import Response


class FailFastRequestBehavior(Generic[Request, TResponse]): # type: ignore
    def __init__(self, validators: List[Callable[[Request], Awaitable[List[ValidationError]]]]):
        self._validators = validators

    async def _errors(self, failures: List[ValidationErr]) -> Response:
        response = Response()
        for failure in failures:
            response.add_error(str(failure))
        return response

    async def handle(self, request: Request, next: Callable[[], Awaitable[TResponse]], cancellation_token: Any = None) -> TResponse:
        failures = []
        for validator in self._validators:
            if iscoroutinefunction(validator):
                result = await validator(request)
            else:
                result = validator(request)
            failures.extend(result)

        if failures:
            return await self._errors(failures)
        
        return await next()