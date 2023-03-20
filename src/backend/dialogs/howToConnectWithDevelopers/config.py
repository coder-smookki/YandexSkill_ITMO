from utils.responseHelper import getLanguage

config = {
    "ru-RU": {
        "message": """Обращайтесь по общей почте команды - SuperScriptsDebugers@yandex.ru""",
        "tts": """Обращайтесь по общей почте команды - Super. Scripts. Debugers. @ yandex. точка. ru.""",
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
    },
    "en-US": {
        "message": """Contact the team by general mail - SuperScriptsDebugers@yandex.ru""",
        "tts": """Contact the team by general mail - Super. Scripts. debuggers. @yandex. dot. ru.""",
        "buttons": [
            "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
    },
}

session_state = {"branch": "howToConnectWithDevelopers"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "message": config[lang]["message"],
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "session_state": session_state,
    }
