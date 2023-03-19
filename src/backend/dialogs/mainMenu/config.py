from utils.responseHelper import getGlobalState, getLanguage
from utils.triggerHelper import haveGlobalState

config = {
    "ru-RU": {
        "tts": """
        Ты выбрал Русский Язык! 
        Хотел бы заранее предупредить вас, что навык может работать некорректно голосом! Приносим наши извинения и будем стараться делать навык всё лучше и лучше для голосового пользования!
        Преобладает использование - текстовое.
        Выберите нужную категорию, которая поможет тебе.
        Первое - это Новости.
        Второе - это Студенческий офис.
        Третье - это Первокурсникам.
        Четвёртое - это Расписание занятий.
        Шестое - это Иностранному студенту.
        Седьмое - это Общеуниверситетские модули в бакалавриате.
        Восьмое - это Общеуниверситетские модули в магистратуре.
        Девятое - это Библиотека.
        Десятое - это Учебные и методические издания.
        Одиннадцатое - это Стипендии.
        Двенадцатое - это Задать вопрос.
        Если такой категории нет, скажите "задать вопрос" и затем заполните всю информацию, чтобы мы могли знать, чего не хватает в навыке.
        """,
        "buttons": [
            "Новости",
            "Студенческий офис",
            "Первокурсникам",
            "Расписание занятий",
            "Расписание сессии",
            "Общеуниверситетские модули в бакалавриате",
            "Общеуниверситетские модули в магистратуре",
            "Библиотека",
            "Учебные и методические издания",
            "Стипендии",
            "Шахматы",
            "Викторина",
            "Случайный факт",
            'Сменить язык',
            'Что ты умеешь?',
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "КАТАЛОГ",
            "description": """
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
            """,
        },
    },
    "en-US": {
        "tts": """
        You chose English language! 
        Choose the right category that will help you.
        1. News
        2. Student Office
        3. For freshmen
        4. Class schedule
        5. Session schedule
        6. For international students
        7. University-wide modules in the Bachelor's degree
        8. University-wide modules in the Master's program
        9. Library
        10. Educational and methodological publications
        11. scholarships
        12. Ask a question
        If there is no such category, say "ask a question" and then fill in all the information so that we can know what is missing in the skill.
        """,
        "buttons": [
            "News",
            "Студенческий офис",
            "Первокурсникам",
            "Расписание занятий",
            "Иностранному студенту",
            "Общеуниверситетские модули в бакалавриате",
            "Общеуниверситетские модули в магистратуре",
            "Библиотека",
            "Учебные и методические издания",
            "Стипендии",
            "Change language",
            "Chess",
            "Quiz",
            "Random Fact",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "CATALOG",
            "description": """
            You chose English language! 
            Choose the right category that will help you.
            1. News
            2. Student Office
            3. For freshmen
            4. Class schedule
            5. Session schedule
            6. For international students
            7. University-wide modules in the Bachelor's degree
            8. University-wide modules in the Master's program
            9. Library
            10. Educational and methodological publications
            11. scholarships
            12. Ask a question
            If there is no such category, say "ask a question" and then fill in all the information so that we can know what is missing in the skill.
            """,
        },
    }
}

session_state = {"branch": "mainMenu"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
        "user_state_update": {
            "language": lang
        },
    }
