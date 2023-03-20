from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Друзья. Поздравляем! Стартовал ваш первый учебный год в Университете ИТМО!
            Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке.
            Чтобы всегда быть в теме, скачивайте полезные мобильные приложения для студентов Университета ИТМО.
            Приложение на айос и на андроид называется - my, точка, itmo.
            """,
        "buttons": [
            {
                'title': 'Официальный сайт',
                'url': 'https://student.itmo.ru/ru/',
                'hide': False
            },
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выйти"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '965417/877ccf979621f858aefe',
            'title': 'ПЕРВОКУРСНИКАМ',
            'description': \
                """
                Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке.
                """
        }
    },

    "en-US": {
        "tts":
            """
            Friends. Congratulations! Your first academic year at ITMO University has started!
            All questions that arise during the training can be solved by clicking on the link.
            To always be in the know, download useful mobile apps for ITMO University students.
            The application for iOS and Android is called - my, dot, itmo.
            """,
        "buttons": [
            {
                'title': 'Official site',
                'url': 'https://student.itmo.ru/ru/',
                'hide': False
            },
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '965417/877ccf979621f858aefe',
            'title': 'FRESHENERS',
            'description': \
                """
                All questions that arise during the training can be solved by clicking on the link.
                """
        }
    }
}
session_state = {
    "branch": "forFreshman"
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
