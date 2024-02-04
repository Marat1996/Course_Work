from abc import ABC, abstractmethod


class APIConnector(ABC):
    """Класс для работы с API"""

    @abstractmethod
    def __init__(self, keyword: str):
        self.__parameters = {}

    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        pass
