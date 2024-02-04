from abc import ABC, abstractmethod
import json


class Saver(ABC):
    """Абстрактный класс для получения вакансий"""

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def get_vacancies(self, vacancies) -> None:
        pass


class JSONSaver(Saver):
    """Записывает вакансии в файл json"""

    def get_vacancies(self, vacancies):
        all_vacancies = [vacancy.to_dict() for vacancy in vacancies]
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(all_vacancies, file, indent=4, ensure_ascii=False)
