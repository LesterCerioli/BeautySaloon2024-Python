

from typing import Optional
from venv import logger
from tenacity import before_sleep_log, retry, stop_after_attempt, wait_exponential
from application.handlers.cities.createcitycommand import CreateCityCommand
from application.services.contracts.icityappservice import ICityAppService
from application.viewmodels.cityviewmodel import CityViewModel
from domain.contracts.icityrepository import ICityRepository


class CityAppService(ICityAppService):
    def __init__(self, city_repository: ICityRepository):
        self._city_repository = city_repository

    async def get_by_city_name(self, city_name: str) -> Optional[CityViewModel]:
        city = await self._city_repository.get_by_city_name(city_name)
        if city:
            return CityViewModel.from_orm(city)
        return None

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        before_sleep=before_sleep_log(logger, "INFO"),
        reraise=True
    )
    async def save(self, command_create: CreateCityCommand) -> None:
        await self._city_repository.add(command_create.to_entity())
        logger.info("City added successfully.")