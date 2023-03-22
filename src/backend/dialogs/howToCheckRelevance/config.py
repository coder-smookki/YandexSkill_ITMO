from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "message":
            """
Наш навык в настоящее время полностью актуален и полностью работоспособен.
Если у вас возникли ошибки с каким-либо блоком навыка, сообщите об ошибке на электронную почту команды.
Таким образом, вы можете помочь поддерживать работоспособность навыка!
            """,
        "tts":
            """
Наш навык в настоящее время полностью актуален и полностью работоспособен.
Если у вас возникли ошибки с каким-либо блоком навыка, сообщите об ошибке на электронную почту команды. super. scripts. debugers. @ yandex. точка. ru
Таким образом, вы можете помочь поддерживать работоспособность навыка!
            """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Назад", "Выйти"],
    },
    "en-US": {
        "message":
            """
Our skill is currently fully relevant and fully functional.
If you have any errors with any skill block, report the error to the team's email. super. scripts. debugers. @ yandex. point. ru
This way, you can help keep the skill working!
            """,
        "tts":
            """
            Our skill is currently fully relevant, and is also fully operational.
            If suddenly you have errors with one or another skill block, report the error by mail to the team's general mail.
            This way you can help keep the skill fully functional!
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

session_state = {"branch": "howToCheckRelevance"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "message": config[lang]["message"],
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "session_state": session_state,
    }
