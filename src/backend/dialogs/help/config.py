from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Выберите раздел, который вам поможет в решение вашего вопроса.
            Кто создатели навыка?
            Как связаться с разработчиками?
            Как узнать актуальность навыка на данный момент?
            Подробнее о навыке.
            На все эти вопросы и уточнения, вы можете получить ответ, если спросите у навыка интересующий вами вопрос.
            """,
        "buttons": [
            "Кто создатели навыка?",
            "Как связаться с разработчиками?",
            "Как узнать актуальность навыка на данный момент?",
            "Подробнее о навыке",
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
Выберите раздел, который вам поможет в решение вашего вопроса или уточнения.
Кто создатели навыка?
Как связаться с разработчиками?
Как узнать актуальность навыка на данный момент?
Подробнее о навыке.
                """,
        },
    },
    "en-US": {
        "tts":
            """
            Choose a section that will help you in solving your question or clarification.
            Who are the creators of the skill?
            How to contact the developers?
            How to find out the relevance of a skill at the moment?
            Learn more about the skill.
            To all these questions, you can get an answer if you ask the skill the question you are interested in.
            """,
        "buttons": [
            "Who are the creators of the skill?",
            "How to contact the developers?",
            "How to find out the relevance of a skill at the moment?",
            "Learn more about the skill",
            "Repeat",
            "What can you do?",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/ffc9c8afbe8b9f6f95c9",
            "title": "HELP",
            "description":
                """
Choose a section that will help you in solving your question or clarification.
Who are the creators of the skill?
How to contact the developers?
How to find out the relevance of a skill at the moment?
Learn more about the skill.
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
