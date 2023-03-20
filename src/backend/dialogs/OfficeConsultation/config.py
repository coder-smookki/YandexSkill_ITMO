from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts": """
            Приходите к нам в офис, расположенный в г. Санкт-Петербург по адресу ул. Ломоносова, д.9. Менеджеры примут вас в порядке живой очереди. Также вы можете записаться на консультацию через приложение «Электронная очередь» в личном кабинете ИСУ.
            """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/65fa68f782fa6af3f071",
            "title": "КАК ПОПАСТЬ НА КОНСУЛЬТАЦИЮ В СТУДЕНЧЕСКИЙ ОФИС?",
            "description": """
                    Приходите к нам в офис, расположенный по адресу ул. Ломоносова, д.9. Менеджеры примут вас в порядке живой очереди. Также вы можете записаться на консультацию через приложение «Электронная очередь» в личном кабинете ИСУ.
                """,
        },
    },
    "en-US": {
        "tts": """
            Come to our office located in St. Petersburg at st. Lomonosov, d.9. Managers will receive you on a first-come, first-served basis. You can also sign up for a consultation through the Electronic Queue application in your UIS personal account.""",
        "buttons": [
            "Announcements",
            "Contests",
            "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "HOW TO GET THE CONSULTATION IN THE STUDENT OFFICE?",
            "description": """
                    Come to our office located in St. Petersburg at st. Lomonosov, d.9. Managers will receive you on a first-come, first-served basis. You can also sign up for a consultation through the Electronic Queue application in your UIS personal account.""",
        },
    },
}

session_state = {"branch": "OfficeConsultation"}


def getConfig(event):
    lang = getLanguage(event)

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
