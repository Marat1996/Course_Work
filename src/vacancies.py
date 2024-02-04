class Vacancy:
    """Собирает данные о вакансиях с разных источников"""

    def __init__(self,
                 vacancy_title: str,
                 vacancy_city: str,
                 salary_from: int,
                 salary_to: int,
                 vacancy_responsibilities: str,
                 vacancy_url: str
                 ):
        self.vacancy_title = vacancy_title  # заголовок вакансии
        self.vacancy_city = vacancy_city  # город
        self.salary_from = self.confirm_salary(salary_from)  # заработанная плата от
        self.salary_to = self.confirm_salary(salary_to)  # заработанная плата до
        self.total_salary = self.general_salary(salary_from, salary_to)  # заработанная плата итого
        self.vacancy_responsibilities = vacancy_responsibilities  # должностные обязанности
        self.vacancy_url = vacancy_url  # ссылка на вакансию

    @staticmethod
    def confirm_salary(salary):
        """Проверка заработанной платы"""
        if salary is None:
            return 0
        return salary

    def general_salary(self, salary_from: object, salary_to: object) -> object:
        return f'{self.confirm_salary(salary_from)} - {self.confirm_salary(salary_to)}'

    def to_dict(self):
        """Возвращает вакансию в виде словаря"""
        return {"vacancy_title": self.vacancy_title,
                "vacancy_city": self.vacancy_city,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "vacancy_responsibilities": self.vacancy_responsibilities,
                "vacancy_url": self.vacancy_url}

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from > other.salary_from

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from != other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from >= other.salary_from


class VacancyHeadHunter(Vacancy):
    """Класс, указывающий с какой платформы вакансия"""

    def __init__(self,
                 vacancy_title: str,
                 vacancy_city: str,
                 salary_from: int,
                 salary_to: int,
                 vacancy_responsibilities: str,
                 vacancy_url: str
                 ):
        super().__init__(vacancy_title,
                         vacancy_city,
                         salary_from,
                         salary_to,
                         vacancy_responsibilities,
                         vacancy_url)
        self.platform = "HeadHunter"

    def __str__(self):
        return f"Вакансия с HeadHunter: {self.vacancy_title}"

    def to_json(self):
        vacancy = super().to_dict()
        vacancy['platfom'] = 'HeadHunter'
        return vacancy


class VacancySuperJob(Vacancy):
    """Класс, указывающий с какой платформы вакансия"""

    def __init__(self,
                 vacancy_title: str,
                 vacancy_city: str,
                 salary_from: int,
                 salary_to: int,
                 vacancy_responsibilities: str,
                 vacancy_url: str
                 ):
        super().__init__(vacancy_title,
                         vacancy_city,
                         salary_from,
                         salary_to,
                         vacancy_responsibilities,
                         vacancy_url)
        self.platform = "SuperJob"

    def __str__(self):
        return f"Вакансия с SuperJob: {self.vacancy_title}"

    def to_json(self):
        vacancy = super().to_dict()
        vacancy['platfom'] = 'SuperJob'
        return vacancy
