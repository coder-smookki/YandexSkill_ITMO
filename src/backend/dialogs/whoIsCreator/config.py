from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "message": """
        Ильин Кирилл (Тимлид).
        Плюснин Александр (Главный Разработчик).
        Караваев Иван (Разработчик).
        Лесовой Кирилл (Тестировщик).
        Кутников Родион (Дизайнер UI|UX).
        """,
        "tts": """ 
        Создатели навыка: Ильин Кирилл, исполняет роль Тим Лидера. 
        Плюснин Александр, исполняет роль Главного Разработчика навыка и его основы. 
        Караваев Иван, исполняет роль Разработчика. Лесовой Кирилл, 
        исполняет роль Тестировщика навыка и Разработчика по алгоритмизации игр. 
        Кутников Родион, исполняет роль Главного Дизайнера в проекте, в том числе UI и UX.
        """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
    },
    "en-US": {
        "message": """
        Ilyin Kirill (Teamlead).
        Plusnin Alexander (Chief Developer).
        Karavaev Ivan (Developer).
        Lesovoy Kirill (Tester).
        Kutnikov Rodion (UI|UX Designer).
        """,
        "tts": """
        Skill creators: Ilyin Kirill, plays the role of Team Leader.
        Plyusnin Alexander, plays the role of the Chief Developer of the skill and its basis.
        Karavaev Ivan, plays the role of Developer. Lesovoy Kirill,
        Acts as Skill Tester and Game Algorithm Developer.
        Kutnikov Rodion, plays the role of Chief Designer in the project, including UI and UX.
        """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
    },
}

session_state = {"branch": "whoIsCreator"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "message": config[lang]["message"],
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "session_state": session_state,
    }
