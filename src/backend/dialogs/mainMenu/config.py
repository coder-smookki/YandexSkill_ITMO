from utils.responseHelper import getGlobalState, getLanguage
from utils.triggerHelper import haveGlobalState

config = {
    "ru-RU": {
        "tts": """
        Хотел бы заранее предупредить вас, что навык может работать некорректно голосом! Приносим наши извинения и будем стараться делать навык всё лучше и лучше для голосового пользования!
        Выберите нужную категорию, которая поможет вам.
        Новости,
        Студенческий офис,
        Первокурсникам,
        Расписание занятий,
        Общеуниверситетские модули в бакалавриате,
        Общеуниверситетские модули в магистратуре,
        Иностранному студенту,
        Библиотека,
        Учебные и методические издания,
        Стипендии,
        Шахматы,
        Викторина,
        Случайный факт,
        """,
        "buttons": [
            "Новости",
            "Студенческий офис",
            "Первокурсникам",
            "Расписание занятий",
            "Общеуниверситетские модули в бакалавриате",
            "Общеуниверситетские модули в магистратуре",
            'Иностранному студенту',
            "Библиотека",
            "Учебные и методические издания",
            "Стипендии",
            "Шахматы",
            "Викторина",
            "Случайный факт",
            'Шахматы',
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
            Выберите нужную категорию, которая поможет вам.
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
            "Student office",
            "Freshmen",
            "Timetable of classes",
            "For a foreign student",
            "University-wide undergraduate modules",
            "University-wide modules in the master's program",
            "Library",
            "Educational and methodical publications",
            "Scholarships",
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
