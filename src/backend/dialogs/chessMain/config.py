message = tts = \
    """
Шахматы! Правила просты: называешь клетку откуда и клетку куда, а потом я делаю ход.
Скажи "Да" или "Играть", чтобы начать, или "Правила", чтобы прочитать правила. 
    """

buttons = [
    "Играть",
    "Помощь",
    "Назад",
    "Выйти"
]

rules = rules_tts = \
    """
Шахматные правила.
...
Скажи "Да" или "Играть", чтобы начать играть.
    """

card = dict()

session_state = {
    "branch": "chessMain",
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }


def getHelpConfig():
    return {
        'message': rules,
        'tts': rules_tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
