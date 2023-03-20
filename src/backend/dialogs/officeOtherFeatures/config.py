from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Конечно! Помимо перечисленных вопросов, вы можете получить информацию о: оплате обучения, учебном процессе, получении места в общежитии или переселении. И другие.
            """,
        "buttons": [
            "Повторить ещё раз",
            'Что ты умеешь?',
            "Помощь",
            "Назад",
            "Выйти"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '1521359/65fa68f782fa6af3f071',
            'title': 'ДРУГИЕ ВОЗМОЖНОСТИ',
            'description': \
                """
                Конечно! Помимо перечисленных вопросов, вы можете получить информацию о: оплате обучения, учебном процессе, получении места в общежитии/переселении. И др.
                """
        }
    },

    "en-US": {
        "tts":
            """
            Certainly! In addition to the questions listed above, you can get information about:
tuition fees;
educational process;
obtaining a place in a hostel / resettlement.
And other
            """,
        "buttons": [
            "Repeat one more time",
            'What can you do?',
            "Help",
            "Back",
            "Go out"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '937455/40f0536e426907808499',
            'title': 'Other Features',
            'description': \
                """
        Certainly! In addition to the questions listed above, you can get information about:
        tuition fees;
        educational process;
        obtaining a place in a hostel / resettlement.
        And etc.
                """
        }
    }
}

session_state = {
    "branch": "officeOtherFeatures"
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
