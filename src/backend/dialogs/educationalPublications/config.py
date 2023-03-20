from utils.responseHelper import getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Скажите или напишите издание, которое вы хотите найти.
            """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "997614/e38bbfd1a2235c7229b1",
            "title": "УЧЕБНЫЕ ИЗДАНИЯ",
            "description":
                """
                Скажите или напишите издание, которое вы хотите найти.
                """,
        },
    },
    "en-US": {
        "tts":
            """
            Say or write the edition you want to find.
            """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "EDUCATIONAL PUBLICATIONS",
            "description":
                """
                Say or write the edition you want to find.
                """,
        },
    },
}

session_state = {"branch": "educationalPublications"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
