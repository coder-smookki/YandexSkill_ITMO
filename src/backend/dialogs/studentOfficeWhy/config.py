from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Через студенческий офис вы можете:
    получить любую справку.
    продлить или заменить студенческий билет.
    заменить паспортные данные.
    продлить сессию по уважительной причине.
    подать заявление на академический отпуск, перевод, восстановление, отчисление.
    временно получить свой документ об образовании. Аттестат или диплом.
            """,
        "buttons": [
            "Повторить ещё раз",
            'Что ты умеешь?',
            "Помощь",
            "Назад",
            "Выйти",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '1521359/65fa68f782fa6af3f071',
            'title': 'ЗАЧЕМ МНЕ ОБРАЩАТЬСЯ В СТУДЕНЧЕСКИЙ ОФИС?',
            'description': \
                """
                Через студенческий офис вы можете: получить любую справку, продлить/заменить студенческий билет; заменить паспортные данные, продлить сессию по уважительной причине, подать заявление на академический отпуск / перевод / восстановление / отчисление, временно получить свой документ об образовании (аттестат/диплом).
                """
        }
    },

    "en-US": {
        "tts":
            """
            Through the student office, you can:
     get any help.
     extend or replace your student card.
     replace passport data.
     extend the session for a good reason.
     apply for academic leave, transfer, restoration, expulsion.
     temporarily receive your document on education. Certificate or diploma.
            """,
        "buttons": [
            "Repeat one more time",
            'What can you do?',
            "Help",
            "Back",
            "Exit",
        ],

        "card": {
            'type': 'BigImage',
             'image_id': '1521359/65fa68f782fa6af3f071',
             'title': 'WHY SHOULD I GO TO THE STUDENT OFFICE?',
             'description': \
                 """
                 Through the student office you can: get any certificate, extend/replace your student card; replace passport data, extend the session for a good reason, apply for academic leave / transfer / restoration / expulsion, temporarily receive your education document (certificate / diploma).
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
