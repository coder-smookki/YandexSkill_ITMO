message = \
    """
    Создатели навыка:
        Ильин Кирилл
        Плюснин Александр
        Караваев Иван
        Лесовой Кирилл
        Кутников Родион
    """

tts = \
    """ 
    Создатели навыка:
        Ильин Кирилл
        Плюснин Александр
        Караваев Иван
        Лесовой Кирилл
        Кутников Родион
    """

buttons = [
    "Назад",
    "Выйти"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'СОЗДАТЕЛИ НАВЫКА',
    'description':
    """
        Создатели навыка:
        Ильин Кирилл
        Плюснин Александр
        Караваев Иван
        Лесовой Кирилл
        Кутников Родион
    """
}

session_state = {
    "branch": "howToConnectWithDevelopers"
}

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
