message = \
    """
    Вы перешли в раздел "что ты умеешь"
    """

tts = \
    """ 
    Вы перешли в раздел "что ты умеешь".
    """

buttons = [
    "Кто создатели навыка?",
    "Как связаться с разработчиками?",
    "Как узнать актуальность навыка на данный момент?",
    "Повторить ещё раз",
    "Назад",
    "Выйти",
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ПОМОЩЬ',
    'description':
        """
            что ты умеешь
        """
}

session_state = {
    "branch": "whatYouCan"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
