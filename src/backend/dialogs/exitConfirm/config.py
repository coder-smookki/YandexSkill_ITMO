message = \
    """
    Вы уверены в том, что хотите выйти?
    """
 
tts = \
    """
    Вы уверены в том, что хотите выйти?
    """

buttons = [
    "Да",
    "Нет",
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ВЫ УВЕРЕНЫ?',
    'description': \
        """
        Вы уверены в том, что хотите выйти?
        """
}

session_state = {
    "branch": "exitConfirm"
}

end_session = True

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
