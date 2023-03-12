message = \
    """
    Вы направились в категорию "Новости"

    """

tts = \
    """
    Вы направились в категорию "Новости"
    """

buttons = [
    "Анонсы",
    "Контесты",
    "Назад",
    "Выйти",
    "Помощь"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'НОВОСТИ',
    'description': \
        """
        Вы направились в категорию "Новости"
        """
}

session_state = {
    "branch": "news"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
