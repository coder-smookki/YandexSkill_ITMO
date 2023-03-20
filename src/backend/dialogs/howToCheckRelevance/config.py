from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "message": """Наш навык имеет на данный момент полную актуальность, а так же является полностью рабочим. 
Если вдруг у вас возникли ошибки с тем или иным блоком навыка, сообщите ошибку по почте общей почте команды. 
Таким образом, вы можете помочь держать навык полностью функциональным!""",
        "tts": """Наш навык имеет на данный момент полную актуальность, а так же является полностью рабочим. 
Если вдруг у вас возникли ошибки с тем или иным блоком навыка, сообщите ошибку по почте общей почте команды. 
Таким образом, вы можете помочь держать навык полностью функциональным!""",
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Назад", "Выйти"],
    },
    "en-US": {
        "tts": """
            Our skill is currently fully relevant, and is also fully operational. If suddenly you have errors with one or another skill block, report the error to Team Leader Ilyin Kirill. this way you can help keep the skill fully functional!
            """,
        "buttons": [
            "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "ACTUALITY",
            "description": """
                Our skill is currently fully relevant, and is also fully operational. If suddenly you have errors with one or another skill block, report the error to Team Leader Ilyin Kirill. this way you can help keep the skill fully functional!
                """,
        },
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
