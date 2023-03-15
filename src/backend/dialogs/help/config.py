message = \
    """
    Вы перешли в раздел "Помощь"

    Выберите раздел, который вам поможет в решение вашего вопроса.
    Кто создатели навыка?
    Как связаться с разработчиками?
    Как узнать актуальность навыка на данный момент?
    """

tts = \
    """ 
    Вы перешли в раздел "Помощь".
    Выберите раздел, который вам поможет в решение вашего вопроса.
    Кто создатели навыка?
    Как связаться с разработчиками?
    Как узнать актуальность навыка на данный момент?
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
        Выберите раздел, который вам поможет в решение вашего вопроса.
        Кто создатели навыка?
        Как связаться с разработчиками?
        Как узнать актуальность навыка на данный момент?
    """
}

session_state = {
    "branch": "help"
}

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
