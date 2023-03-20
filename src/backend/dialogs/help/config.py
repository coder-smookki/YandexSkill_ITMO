from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Выберите раздел, который вам поможет в решение вашего вопроса.
            Кто создатели навыка?
            Как связаться с разработчиками?
            Как узнать актуальность навыка на данный момент?
            На все эти вопросы, вы можете получить ответ, если спросите у навыка интересующий вами вопрос.
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
            "type": "BigImage",
            "image_id": "1521359/ffc9c8afbe8b9f6f95c9",
            "title": "ПОМОЩЬ",
            "description":
                """
                Выберите раздел, который вам поможет в решение вашего вопроса.
                Кто создатели навыка?
                Как связаться с разработчиками?
                Как узнать актуальность навыка на данный момент?
                """,
        },
    },
    "en-US": {
        "tts":
            """
            Select the section that will help you answer your question.
            Who are the creators of the skill?
            How to contact the developers?
            How to find out the relevance of a skill at the moment?
            To all these questions, you can get an answer if you ask the skill the question you are interested in.
            """,
        "buttons": [
            "Who are the creators of the skill?",
            "How to contact the developers?",
            "How to find out the relevance of a skill at the moment?",
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/ffc9c8afbe8b9f6f95c9",
            "title": "HELP",
            "description":
                """
                Select the section that will help you resolve your issue.
                Who are the creators of the skill?
                How to contact the developers?
                How to find out the relevance of a skill at the moment?
                """,
        },
    },
}

session_state = {"branch": "help"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
