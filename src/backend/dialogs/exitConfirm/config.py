from utils.responseHelper import getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Вы уверены в том, что хотите выйти?
            """,
        "buttons": [
            "Да",
            "Нет",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "997614/ca506e7918d405f24764",
            "title": "ВЫЙТИ ИЗ НАВЫКА?",
            "description":
                """
                Вы уверены в том, что хотите выйти?
                """,
        },
    },
    "en-US": {
        "tts":
            """
            Are you sure you want to exit?
            """,
        "buttons": [
            "Yes",
            "No",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "997614/ca506e7918d405f24764",
            "title": "EXIT SKILL?",
            "description":
                """
                Are you sure you want to exit?
                """,
        },
    },
}

session_state = {"branch": "exitConfirm"}


def getConfig(event):
    lang = getLanguage(event)
    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }


def getConfirmResponse(event):
    lang = getLanguage(event)
    if lang == "ru-RU":
        return {
            "response": {
                "text": "До скорых встреч! Были рады вас видеть в нашем навыке!",
                "tts": "До скорых встреч! Были рады вас видеть в нашем навыке!",
                "buttons": [],
                "end_session": True,
            },
            "version": event["version"],
            "dontUpdateBranches": True,
        }
    else:
        return {
            "response": {
                "text": "See you soon! We were glad to see you in our skill!",
                "tts": "See you soon! We were glad to see you in our skill!",
                "buttons": [],
                "end_session": True,
            },
            "version": event["version"],
            "dontUpdateBranches": True,
        }