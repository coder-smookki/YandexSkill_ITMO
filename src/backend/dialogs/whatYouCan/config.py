from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Вы перешли в раздел "что ты умеешь".
            """,
        "buttons": [
            "Кто создатели навыка?",
            "Как связаться с разработчиками?",
            "Как узнать актуальность навыка на данный момент?",
            "Повторить ещё раз",
            "Помощь",
            "Назад",
            "Выйти",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '937455/40f0536e426907808499',
            'title': 'ПОМОЩЬ',
            'description':
                """
                    что ты умеешь
                """
        }
    },

    "en-US": {
        "tts":
            """
            You have moved to the "what can you do" section.
            """,
        "buttons": [
            "Who are the creators of the skill?",
            "How to contact the developers?",
            "How to find out the relevance of a skill at the moment?",
            "Repeat one more time",
            "Help",
            "Back",
            "Exit",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '965417/877ccf979621f858aefe',
            'title': 'HELP',
            'description': \
                """
                    What can you do                
                """
        }
    }
}

session_state = {
    "branch": "whatYouCan"
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
