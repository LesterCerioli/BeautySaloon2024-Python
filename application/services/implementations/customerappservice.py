

import logging
from typing import Optional

from tenacity import retry, stop_after_attempt, wait_exponential
from application.handlers.customers.createcustomercommand import CreateCustomerCommand
from application.services.contracts.icustomerappservice import ICustomerAppService
from application.viewmodels.customerviewmodel import CustomerViewModel
from domain.contracts.icustomerrepository import ICustomerRepository
from value_objects.telephone import Telephone


class CustomerAppService(ICustomerAppService):
    def __init__(self, customer_repository: ICustomerRepository, mapper, mediator, logger: logging.Logger):
        self._customer_repository = customer_repository
        self._mapper = mapper
        self._mediator = mediator
        self._logger = logger

    async def get_by_customer(self, customer_name: str) -> Optional[CustomerViewModel]:
        customer_entity = await self._customer_repository.get_by_customer(customer_name)
        return self._mapper.to_viewmodel(customer_entity)

    async def get_by_email(self, email: str) -> Optional[CustomerViewModel]:
        customer_entity = await self._customer_repository.get_by_email(email)
        return self._mapper.to_viewmodel(customer_entity)

    async def get_by_telephone(self, telephone: Telephone) -> Optional[CustomerViewModel]:
        customer_entity = await self._customer_repository.get_by_telephone(telephone)
        return self._mapper.to_viewmodel(customer_entity)

    @retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
    async def save(self, command_create: CreateCustomerCommand):
        try:
            await self._customer_repository.add(command_create.get_entity())
            self._logger.info("Customer added successfully.")
        except Exception as e:
            self._logger.warning(f"Retrying due to: {str(e)}")
            raise