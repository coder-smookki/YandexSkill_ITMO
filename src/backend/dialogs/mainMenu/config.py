from utils.responseHelper import getGlobalState, getLanguage
from utils.triggerHelper import haveGlobalState

config = {
    "ru-RU": {
        "tts":
            """
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
            "Иностранному студенту",
            "Библиотека",
            "Учебные и методические издания",
            "Стипендии",
            "Шахматы",
            "Викторина",
            "Случайный факт",
            "Сменить язык",
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "965417/6964866b174321bd8721",
            "title": "КАТАЛОГ",
            "description":
                """
                Выберите нужную категорию, которая поможет вам.
                """,
        },
    },
    "en-US": {
        "tts":
            """
            Choose the right category to help you.
            News,
            student office,
            Freshmen
            Timetable of classes,
            University-wide undergraduate modules,
            University-wide modules in the magistracy,
            foreign student,
            Library,
            Educational and methodical publications,
            scholarships,
            Chess,
            Quiz,
            random fact,
            """,
        "buttons": [
            "News",
            "Student Office",
            "For freshmens",
            "Timetable of classes",
            "University-wide modules in undergraduate studies",
            "University-wide modules in the magistracy",
            "Foreign student",
            "Library",
            "Educational and methodical publications",
            "Scholarships",
            "Chess",
            "Quiz",
            "Random Fact",
            "Change language",
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "965417/6964866b174321bd8721",
            "title": "CATALOG",
            "description":
                """
                Choose the right category to help you.
                """,
        },
    },
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
        "user_state_update": {"language": lang},
    }
