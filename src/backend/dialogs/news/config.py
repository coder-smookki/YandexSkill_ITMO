tts = \
    """
    Выберите раздел новостей, которую хотите посмотреть.
    Анонсы или Контесты.
    """

buttons = [
    "Анонсы",
    "Контесты",
    'Что ты умеешь?',
    "Помощь",
    "Назад",
    "Выйти"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'НОВОСТИ',
    'description': \
        """
        Выберите раздел новостей: Анонсы или Контесты.
        """
}

session_state = {
    "branch": "news"
}


def getConfig():
    return {
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
