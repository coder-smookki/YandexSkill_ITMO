message = \
    """
    Напишите вашу группу и курс в формате:
    <группа> <курс>
    """

tts = \
    """
    Скажите вашу группу и курс (Желательно в письменном виде, так как обработка запроса пока не доделана)
    """

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

session_state = {
    "branch": "timeTable"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }