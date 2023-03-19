from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Вы перешли в раздел "Помощь".
            Выберите раздел, который вам поможет в решение вашего вопроса.
            Кто создатели навыка?
            Как связаться с разработчиками?
            Как узнать актуальность навыка на данный момент?
            """,
        "buttons": [
            "Кто создатели навыка?",
            "Как связаться с разработчиками?",
            "Как узнать актуальность навыка на данный момент?",
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выйти",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '1521359/059aaefcfb0a6b5d9cb4',
            'title': 'ПОМОЩЬ',
            'description':
                """
                    Выберите раздел, который вам поможет в решение вашего вопроса.
                    Кто создатели навыка?
                    Как связаться с разработчиками?
                    Как узнать актуальность навыка на данный момент?
                """
        }
    },

    "en-US": {
        "tts":
            """
            You have moved to the "Help" section.
            Select the section that will help you resolve your issue.
            Who are the creators of the skill?
            How to contact the developers?
            How to find out the relevance of a skill at the moment?
            """,
        "buttons": [
            "Who are the creators of the skill?",
            "How to contact the developers?",
            "How to find out the relevance of a skill at the moment?",
            "Repeat one more time",
            "What can you do?",
            "Back",
            "Exit",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '1521359/059aaefcfb0a6b5d9cb4',
            'title': 'HELP',
            'description':
                """
                    Select the section that will help you resolve your issue.
                    Who are the creators of the skill?
                    How to contact the developers?
                    How to find out the relevance of a skill at the moment?
                """


        }
    }
}

session_state = {
    "branch": "help"
}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
