message = \
    """
    Вы уверены в том, что хотите выйти?
    """
 
tts = \
    """
    Вы уверены в том, что хотите выйти из навыка?
    """

buttons = [
    "Да",
    "Нет",
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ВЫЙТИ ИЗ НАВЫКА?',
    'description': \
        """
        Вы уверены в том, что хотите выйти?
        """
}

session_state = {
    "branch": "exitConfirm"
}

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }
