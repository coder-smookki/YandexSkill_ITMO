message = \
    """
    Напишите вашу группу и курс в формате:
    <группа> <курс>
    """

tts = \
    """
    Продиктуйте вашу Группу и Курс. Пример может быть такой (А1234, 4)
    """

buttons = [
    "Повторить ещё раз",
    "Помощь"
    "Назад",
    "Выйти"
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
