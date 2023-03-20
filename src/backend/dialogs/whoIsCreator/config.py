from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        'message': """
        Ильин Кирилл (Тим Лидер).
        Плюснин Александр (Главный Разработчик).
        Караваев Иван (Разработчик).
        Лесовой Кирилл (Тестировщик).
        Кутников Родион (Дизайнер UIㅤ|ㅤUX).
        """,
        "tts":
            """ 
                Создатели навыка: Ильин Кирилл исполняет роль Тим Лидера. Плюснин Александр исполняет роль Главного Разработчика навыка и его основы. Караваев Иван исполняет роль Разработчика. Лесовой Кирилл исполняет роль Тестировщика навыка и Разработчика по +алгоритмизации игр. Кутников Родион исполняет роль Главного Дизайнера в проекте, в том числе UI и UX.
            """,
        "buttons": [
            "Повторить ещё раз",
            'Что ты умеешь?',
            "Назад",
            "Выйти"
        ],
    },

    "en-US": {
        "tts":
            """
            Skill creators: Ilyin Kirill plays the role of Team Leader. Plyusnin Alexander plays the role of the Chief Developer of the skill and its foundation. Karavaev Ivan plays the role of the Developer. Lesovoy Kirill plays the role of Skill Tester and Game Algorithm Developer. Kutnikov Rodion plays the role of Chief Designer in the project, including UI and UX.
            """,
        "buttons": [
            "Repeat one more time",
            'What can you do?',
            "Back",
            "Exit"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '965417/877ccf979621f858aefe',
            'title': 'FRESHENERS',
            'description': \
                """
                Ilyin Kirill (Team Leader).
                Plyusnin Alexander (Chief Developer).
                Karavaev Ivan (Developer).
                Lesovoy Kirill (Tester).
                Kutnikov Rodion (UI Designerㅤ|ㅤUX).
                """
        }
    }
}

session_state = {
    "branch": "whoIsCreator"
}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "message": config[lang]['message'],
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "session_state": session_state,
    }

