from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Через студенческий офис вы м+ожете:
            Получить любую справку.
            Продлить или заменить студенческий билет.
            Заменить паспортные данные.
            Продлить сессию по уважительной причине.
            Подать заявление на академический отпуск, на перевод; восстановление; отчисление.
            Временно получить свой документ об образовании, Аттестат или диплом.
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
            'title': 'ЗАЧЕМ МНЕ ОБРАЩАТЬСЯ В СТУДЕНЧЕСКИЙ ОФИС?',
            'description':
                """
Через студенческий офис вы можете: Получить любую справку. Продлить или заменить студенческий билет. Заменить паспортные данные.
Продлить сессию по уважительной причине. Подать заявление на академический отпуск, перевод, восстановление, отчисление.
Временно получить свой документ об образовании. Аттестат или диплом.
                """
        }
    },

    "en-US": {
        "tts":
            """
            Through the Student Office, you can:
            Get any help.
            Renew or replace student card.
            Replace passport data.
            Extend the session for a good reason.
            Apply for academic leave, for transfer; recovery; deduction.
            Temporarily receive your document of education, Certificate or diploma.
            """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],

        "card": {
            'type': 'BigImage',
             'image_id': '1521359/65fa68f782fa6af3f071',
             'title': 'WHY SHOULD I GO TO THE STUDENT OFFICE?',
             'description':
                 """
Through the student office you can: Get any certificate. Renew or replace student card. Replace passport data.
Extend the session for a good reason. Apply for academic leave, transfer, restoration, expulsion.
Temporarily receive your document on education. Certificate or diploma.
                 """
        }
    }
}

session_state = {
    "branch": "studentOfficeWhy"
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
