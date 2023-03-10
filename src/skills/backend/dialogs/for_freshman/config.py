message = \
"""
Вы направились в категорию "Первокурсникам"

Друзья, поздравляем! Стартовал ваш первый учебный год  в Университете ИТМО!

Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке - https://student.itmo.ru/ru/. Например, узнать о процессе обучения в ИТМО, можно по ссылке  -https://student.itmo.ru/ru/edu_time/.

Мобильные приложения
Чтобы всегда быть в теме, скачивайте полезные мобильные приложения для студентов Университета ИТМО:

Приложение на IOS  называется - my.itmo
Приложение на Android называется - my.itmo
"""

tts = \
"""
Вы направились в категорию "Первокурсникам"

Друзья, поздравляем! Стартовал ваш первый учебный год  в Университете ИТМО!

Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке - https://student.itmo.ru/ru/. Например, узнать о процессе обучения в ИТМО, можно по ссылке  -https://student.itmo.ru/ru/edu_time/.

Мобильные приложения
Чтобы всегда быть в теме, скачивайте полезные мобильные приложения для студентов Университета ИТМО:

Приложение на IOS  называется - my.itmo
Приложение на Android называется - my.itmo
"""

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ПЕРВОКУРСНИКАМ',
    'description': \
    """
    Вы направились в категорию "Первокурсникам"
    Друзья, поздравляем! Стартовал ваш первый учебный год  в Университете ИТМО!
    Все вопросы, возникающие во время обучения, можно решить если перейти по ссылке - https://student.itmo.ru/ru/. Например, узнать о процессе обучения в ИТМО, можно по ссылке  -https://student.itmo.ru/ru/edu_time/.
    Мобильные приложения
    Чтобы всегда быть в теме, скачивайте полезные мобильные приложения для студентов Университета ИТМО:
    Приложение на IOS  называется - my.itmo
    Приложение на Android называется - my.itmo
    """
}

session_state = {
    "branch": "for_freshman"
}

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
