

from email.headerregistry import Address
import logging
from typing import Optional

from tenacity import retry, stop_after_attempt, wait_exponential
from application.handlers.saloons.createsalooncommand import CreateSaloonCommand
from application.services.contracts.isaloonappservice import ISaloonAppService
from application.viewmodels.saloonviewmodel import SaloonViewModel
from domain.contracts.isaloonrepository import ISaloonRepository
from value_objects.district import District


class SaloonAppService(ISaloonAppService):
    def __init__(self, saloon_repository: ISaloonRepository, mapper, mediator, logger: logging.Logger):
        self._saloon_repository = saloon_repository
        self._mapper = mapper
        self._mediator = mediator
        self._logger = logger

    async def get_by_address(self, address: Address) -> Optional[SaloonViewModel]:
        saloon_entity = await self._saloon_repository.get_by_address(address)
        return self._mapper.to_viewmodel(saloon_entity)

    async def get_by_district(self, district: District) -> Optional[SaloonViewModel]:
        saloon_entity = await self._saloon_repository.get_by_district(district)
        return self._mapper.to_viewmodel(saloon_entity)

    async def get_by_fantasy_name(self, fantasy_name: str) -> Optional[SaloonViewModel]:
        saloon_entity = await self._saloon_repository.get_by_fantasy_name(fantasy_name)
        return self._mapper.to_viewmodel(saloon_entity)

    @retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
    async def save(self, command_create: CreateSaloonCommand):
        try:
            await self._saloon_repository.add(command_create.get_entity())
            self._logger.info("Saloon added successfully.")
        except Exception as e:
            self._logger.warning(f"Retrying due to: {str(e)}")
            raise
