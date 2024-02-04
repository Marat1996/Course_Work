from platform import platform

from src.vacancies import Vacancy, VacancyHeadHunter, VacancySuperJob


def get_vacancy_hh(vacancies: list[dict]):
    """Все найденные вакансии с HeadHunter
    записали в переменную с полями: заголовок вакансии,
                                    город,
                                    заработанная плата от/до,
                                    должностные обязанности,
                                    ссылка на вакансию"""

    list_vacancies = []
    for vacancy in vacancies:
        sample_vacancy = VacancyHeadHunter(
            vacancy_title=vacancy['name'],
            vacancy_city="Город не указан" if (vacancy['address']) is None else vacancy['address']['city'],
            salary_from=vacancy['salary']['from'],
            salary_to=vacancy['salary']['to'],
            vacancy_responsibilities=vacancy['snippet']['responsibility'],
            vacancy_url=vacancy['alternate_url']
        )
        list_vacancies.append(sample_vacancy)
    return list_vacancies


def get_vacancy_sj(vacancies: list[dict]):
    """Все найденные вакансии с SuperJob
    записали в переменную с полями: заголовок вакансии,
                                    город,
                                    заработанная плата от/до,
                                    должностные обязанности,
                                    ссылка на вакансию"""

    list_vacancies = []
    for vacancy in vacancies:
        sample_vacancy = VacancySuperJob(
            vacancy_title=vacancy['profession'],
            vacancy_city="Город не указан" if (vacancy['town']) is None else vacancy['town']['title'],
            salary_from=vacancy['payment_from'],
            salary_to=vacancy['payment_to'],
            vacancy_responsibilities=vacancy['candidat'],
            vacancy_url=vacancy['link']
        )
        list_vacancies.append(sample_vacancy)
    return list_vacancies


def platform_selection():
    """Позволяет выбрать платформу для поиска вакансии"""
    while True:
        platform = ''
        platform_option = input('Выберите платформу для поиска вакансий:\n'
                                '0 - Затрудняюсь ответить\n'
                                '1 - HeadHunter\n'
                                '2 - SuperJob\n'
                                'Введите цифру: ')
        if platform_option == '0':
            platform = None
            break
        elif platform_option == '1':
            platform = 'HeadHunter'
            break
        elif platform_option == '2':
            platform = 'SuperJob'
            break
        else:
            print('Вы ввели неверное значение')
            continue
    return platform


def filtered_vacancies_minimal_salary(vacancies: list[Vacancy], min_salary=0):
    """Фильтрует вакансии по минимальной заработанной плате"""
    sort_vacancies = []
    for vacancy in vacancies:
        if int(vacancy.salary_from) >= 0:
            sort_vacancies.append(vacancy)
    return sorted(sort_vacancies)


def filtered_salary():
    """Фильтрует, введенную пользователем, минимальную заработанную плату"""
    while True:
        salary = 0
        salary_query = input('Введите минимальную заработанную плату: ')
        if not salary_query.isdigit() or int(salary_query) < 0:
            print('Введите целое число')
            continue
        else:
            salary = salary_query
            break
    return int(salary)


def filtered_platform(vacancies, platform):
    """Фильтрует вакансии в выбранной платформе"""
    filtered_vacancies = []
    if platform:
        for vacancy in vacancies:
            if vacancy.platform == platform:
                filtered_vacancies.append(vacancy)
    else:
        filtered_vacancies = vacancies
    return filtered_vacancies


def shows_vacancies(vacancies):
    """Показывает вакансии пользователю"""
    while True:
        top_n = input("Введите количество вакансий для вывода в топ N: ")
        if not top_n.isdigit():
            print("Введите целое число")
            continue
        else:
            top_n = int(top_n)
            break
    print("Мы подобрали для Вас вакансии:\n")
    for vacancy in vacancies[0:top_n]:
        if vacancy.salary_to > 0:
            print(f'Вакансия: {vacancy.vacancy_title}\n'
                  f'Заработанная плата: {vacancy.total_salary}\n'
                  f'Город: {vacancy.vacancy_city}\n'
                  f'Описание: {vacancy.vacancy_responsibilities}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n')
        else:
            print(f'Вакансия: {vacancy.vacancy_title}\n'
                  f'Заработанная плата от: {vacancy.salary_from}\n'
                  f'Город: {vacancy.vacancy_city}\n'
                  f'Описание: {vacancy.vacancy_responsibilities}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n')