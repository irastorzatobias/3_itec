import requests
from typing import Dict, Optional, List


from dataclasses import dataclass
from .models import CovidInfoModel


@dataclass
class CovidInfo:  # dto
    date: Optional[str]
    positive: Optional[int]
    negative: Optional[int]


class CovidGateway:  # Gateway
    _URL_BASE = 'https://api.covidtracking.com'

    def get(self, url: str, *args, **kwargs):
        url = f'{self._URL_BASE}{url}'
        response = requests.get(url)
        return response


class CovidParser:  # Parser
    def values_parser(self, data: Dict) -> dict:
        return data.json()

    def value_parser(self, data: Dict) -> dict:
        return CovidInfo(
            date=data.get('date'),
            positive=data.get('positive'),
            negative=data.get('negative')
        )


class CovidService:  # Servicio
    def __init__(self):
        self.gateway = CovidGateway()
        self.parser = CovidParser()
        self.url = '/v1/us/daily.json'

    def run(self) -> List[CovidInfo]:
        response = self.gateway.get(self.url)
        data = self.parser.values_parser(response)
        covidInfoModel = CovidInfoModel()
        for value in data:
            covidInfo = self.parser.value_parser(value)
            covidInfoModel.create_covid_info(
                covidInfo.date, covidInfo.positive, covidInfo.negative)
