message = ''

tts = ''

buttons = [
    "Повторить ещё раз",
    "Что ты умеешь?",
    "Помощь",
    "Назад",
    "Выйти"
]

session_state = {
    "branch": "announces"
}


def getConfig(lang='ru'):
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }
