message = \
    """
    Ты выбрал Русский Язык! 
    Выбери нужную категорию, которая поможет тебе.
    1. Новости
    2. Студенческий офис
    3. Первокурсникам
    4. Расписание занятий
    5. Расписание сессии
    6. Иностранному студенту
    7. Общеуниверситетские модули в бакалавриате
    8. Общеуниверситетские модули в магистратуре
    9. Библиотека
    10. Учебные и методические издания
    11. Стипендии
    12. Задать вопрос
    Если такой категории нет, скажите "задать вопрос" и затем заполните всю информацию, чтобы мы могли знать, чего не хватает в навыке.
    """

tts = \
    """
    Ты выбрал Русский Язык! 
    Хотел бы заранее предупредить вас, что навык может работать некорректно голосом! Приносим наши извинения и будем стараться делать навык всё лучше и лучше для голосового пользования!
    Преобладает использование - текстовое.
    Выберите нужную категорию, которая поможет тебе.
    Первое - это Новости.
    Второе - это Студенческий офис.
    Третье - это Первокурсникам.
    Четвёртое - это Расписание занятий.
    Пятое - это Расписание сессии.
    Шестое - это Иностранному студенту.
    Седьмое - это Общеуниверситетские модули в бакалавриате.
    Восьмое - это Общеуниверситетские модули в магистратуре.
    Девятое - это Библиотека.
    Десятое - это Учебные и методические издания.
    Одиннадцатое - это Стипендии.
    Двенадцатое - это Задать вопрос.
    Если такой категории нет, скажите "задать вопрос" и затем заполните всю информацию, чтобы мы могли знать, чего не хватает в навыке.
    """

buttons = [
    'Новости',
    'Студенческий офис',
    'Первокурсникам',
    'Расписание занятий',
    'Расписание сессии',
    'Иностранному студенту',
    'Общеуниверситетские модули в бакалавриате',
    'Общеуниверситетские модули в магистратуре',
    'Библиотека',
    'Учебные и методические издания',
    'Стипендии',
    'Задать вопрос',
    'Помощь',
    'Назад',
    'Выйти'
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'КАТАЛОГ'
}

session_state = {
    "branch": "russianMenu"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
