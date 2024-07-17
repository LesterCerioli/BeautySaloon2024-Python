import json
import logging
from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel


from application.handlers.customers.responses.create_customer_response import CreateCustomerResponse
from domain_interfaces.icustomer_repository import ICustomerRepository
from infrastructure.repositories import customer_repository
from validations.customers.create_customer_command_validation import CreateCustomerCommandValidation


class CreateCustomerHandler:
    def __init__(self, customer_repository: ICustomerRepository, logger: logging.Logger):
        self._customer_repository = customer_repository
        self._logger = logger
        
    async def handle(self, command: CreateCustomerCommand) -> CreateCustomerResponse: # type: ignore
        self._logger.info(f"CreateCustomerCommand: {json.dumps(command.dict())}")
        validation_result = CreateCustomerCommandValidation().validate(command)

        if not validation_result.errors():
            try:
                customer_name_exists = await self._customer_repository.get_customer_by_customer_name(command.customer_name)
                telephone_number_exists = await self._customer_repository.get_customer_by_telephone(command.telephone_number)

                if customer_name_exists or telephone_number_exists:
                    return CreateCustomerResponse(command.id, message="Customer already registered!")

                await self._customer_repository.add(command.get_entity())
                return CreateCustomerResponse(command.id, validation_result=validation_result)
            except Exception as ex:
                self._logger.critical(ex, exc_info=True)
                return CreateCustomerResponse(command.id, message="It's not possible to process your solicitation.")

        return CreateCustomerResponse(command.id, validation_result=validation_result)
    

class CustomerEntity(BaseModel):
    customer_name: Optional[str]
    telephone_number: Optional[str]
    

class CreateCustomerCommand(BaseModel):
    id: UUID = uuid4()
    customer_name: Optional[str] = None
    telephone_number: Optional[str] = None
    
    def get_entity(self) -> CustomerEntity:
        return CustomerEntity(
            customer_name=self.customer_name,
            telephone_number=self.telephone_number
        )


class CreateCustomerResponse:
    def __init__(self, request_id: UUID, validation_result: Optional[CreateCustomerCommandValidation] = None, message: Optional[str] = None):
        self.request_id = request_id
        self.validation_result = validation_result
        self.message = message
        self.errors = validation_result.errors() if validation_result else []

    def add_error(self, error: str):
        self.errors.append(error)
