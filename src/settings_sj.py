import requests
import os
from settings import url_superjob
from src.api_connector import APIConnector

from dotenv import load_dotenv

from src.exception import LoadingError

load_dotenv()

superjob_api_key = os.getenv("SJ_API_KEY")


class SuperJobAPI(APIConnector):
    """Получение данных с сайта SuperJob"""

    def __init__(self, keyword: str):
        """Инициализация класса
        keyword = ключевое слово для поиска вакансий"""
        self.keyword = keyword
        self.__parameters = {
            "count": 100,
            "keyword": self.keyword,
            "page": 0,
            "keywords": {
                "srws": 1,
                "skwc": "particular",
                "keys": self.keyword
            }
        }
        self.my_headers = {
            "X-Api-App-Id": superjob_api_key
        }

    @property
    def get_vacancies(self) -> list[dict]:
        """Получение вакансий
        :return: Список с вакансиями"""
        response = requests.get(url=url_superjob, params=self.__parameters, headers=self.my_headers)
        if response.status_code != 200:
            raise LoadingError(f"Ошибка получения вакансий! Статус: {response.status_code}.")
        else:
            return response.json()["objects"]