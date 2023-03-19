from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Вы направились в категорию "Первокурсникам". 
            Друзья. Поздравляем! Стартовал ваш первый учебный год в Университете ИТМО!
            Все вопросы, возникающие во время обучения, можно решить если нажать на кнопку "ИТМО".
            Чтобы всегда быть в теме, скачивайте полезные мобильные приложения для студентов Университета ИТМО.
            Приложение на IOS и на Android называется - my.itmo
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
                Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке
                """
        }
    },

    "en-US": {
        "tts":
            """
            You've made it to the freshman category.
            Friends. Congratulations! Your first academic year at ITMO University has started!
            All questions that arise during the training can be solved by clicking on the "ITMO" button.
            To always be in the know, download useful mobile apps for ITMO University students.
            The application on IOS and on Android is called - my.itmo
            """,
        "buttons": [
            {
                'title': 'Official site',
                'url': 'https://student.itmo.ru/ru/',
                'hide': False
            },
            "Repeat one more time",
            "What can you do?",
            "Help",
            "Back",
            "Exit"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '965417/877ccf979621f858aefe',
            'title': 'FRESHENERS',
            'description': \
                """
                All questions that arise during the training can be solved by clicking on the link
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
        "user_state_update": {
            "language": lang
        },
    }
