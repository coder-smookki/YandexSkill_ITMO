ru_welcome = ru_welcome_tts = \
    """
Шахматы! Правила просты: называешь клетку откуда и клетку куда, а потом я делаю ход.
Скажи "Да" или "Играть", чтобы начать, или "Правила", чтобы прочитать правила.

Важное замечание. Все операции не входят в лимит времени навыков Алисы, поэтому после сообщения о загрузке нужно подождать пару секунд и потом сказать что-угодно.
"""

ru_rules = ru_rules_tts = \
    """
Шахматные правила.
1. Соблюдаются все правила шахмат.
2. Ходы надо говорить в стиле "клетка-клетка", "cNcN", где c - буква, N - номер. Например, e2e4, e-2-e-4, e2-e4 и так далее.
3. Для рокировки надо сказать начальную и конечную клетки.
Скажи "Да" или "Играть", чтобы начать играть.
"""

eng_welcome = eng_welcome_tts = \
    """
Chess! The rules are simple: you name the cell from where and the cell to where, and then I make a move.
Say "Yes" or "Play" to start, or "Rules" to read the rules.

Important note. All operations are not included in the time limit of Alice's skills, so after the message about waiting, you need to wait a couple of seconds and then say anything.
"""

eng_rules = eng_rules_tts = \
    """
Chess rules.
1. All rules of chess are observed.
2. The moves should be said in the style of "cell-cell", "cN", where c is a letter, N is a number. For example: e2e4, e-2-e-4, e2-e4 etc.
3. For castling, it is necessary to say the initial and final cells.
Say "Yes" or "Play" to start playing.
"""

ru_buttons = [
    "Играть",
    "Правила",
    "Назад",
    "Помощь",
    "Выйти"
]

session_state = {
    "branch": "chessMain",
}

messages = {
    "ru-RU": {
        "welcome": ru_welcome,
        "welcome_tts": ru_welcome_tts,
        "rules": ru_rules,
        "rules_tts": ru_rules_tts
    },
    "en-US": {
        "welcome": eng_welcome,
        "welcome_tts": eng_welcome_tts,
        "rules": eng_rules,
        "rules_tts": eng_rules_tts
    }
}


def getConfig(lang: str):
    return {
        'message': messages[lang]['welcome'],
        'tts': messages[lang]['welcome_tts'],
        'buttons': ru_buttons,
        'session_state': session_state
    }


def getHelpConfig(lang: str):
    return {
        'message': messages[lang]['rules'],
        'tts': messages[lang]['rules_tts'],
        'buttons': ru_buttons,
        'session_state': session_state
    }
