import requests
from settings import url_hh
from src.api_connector import APIConnector
from src.exception import LoadingError


class HeadHunterAPI(APIConnector):
    """Получение данных с сайта HeadHunter"""

    def __init__(self, keyword: str):
        """Инициализация класса
        keyword = ключевое слово для поиска вакансий"""
        self.keyword = keyword
        self.__parameters = {
            "per_page": 100,
            "text": self.keyword,
            "search_field": "name",
            "page": 0,
            "only_with_salary": True
        }

    @property
    def get_vacancies(self) -> list[dict]:
        """Получение вакансий
        :return: Список с вакансиями"""
        response = requests.get(url=url_hh, params=self.__parameters)
        if response.status_code != 200:
            raise LoadingError(f"Ошибка получения вакансий! Статус: {response.status_code}.")
        else:
            return response.json()["items"]