message = ''

tts = ''

buttons = [
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"
]

session_state = {
    "branch": "announces"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }
