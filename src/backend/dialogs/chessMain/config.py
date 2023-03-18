message = tts = \
    """
Шахматы! Правила просты: называешь клетку откуда и клетку куда, а потом я делаю ход.
Скажи "Да" или "Играть", чтобы начать, или "Правила", чтобы прочитать правила.

Важное замечание. Все операции не входят в лимит времени навыков Алисы, поэтому после сообщения о загрузке нужно подождать пару секунд и потом сказать что-угодно.
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

session_state = {
    "branch": "chessMain",
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }


def getHelpConfig():
    return {
        'message': rules,
        'tts': rules_tts,
        'buttons': buttons,
        'session_state': session_state
    }
