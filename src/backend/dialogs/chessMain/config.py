message = tts = \
    """
    Шахматы! Правила просты: называешь клетку откуда и клетку куда, а потом я делаю ход.
    Скажи "Да" или "Играть", чтобы начать, или "Правила", чтобы прочитать правила. 
    """

buttons = [
    "Повторить ещё раз",
    "Правила",
    "Помощь",
    "Назад",
    "Выйти"
]

rules = rules_tts = \
    """
    Шахматные правила.
    ...
    Скажи "Да" или "Играть", чтобы начать или продолжить играть.
    """

card = None

session_state = {
    "branch": "chessGame",
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
