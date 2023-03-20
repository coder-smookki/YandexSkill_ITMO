from typing import Any
from itertools import product
import requests
from .config import game, messages
from utils.responseHelper import getState, getLanguage

from .db import get_board_id
from ..chessMain.config import getHelpConfig

api_base = 'http://127.0.0.1:5000/api/chess/'

all_squares = {f'{c}{n}' for c, n in product('abcdefhg', '12345678')}


def is_move(move: str) -> bool:
    return move[:2] in all_squares and move[2:] in all_squares


def replace_scores_to_spaces(strings: list[str]) -> list[str]:
    """
    Когда говоришь Алисе клетку, она принимает её как "c-N" (Е-4, G-3, Д-8),
    а когда говоришь сразу две клетки (ход), она принимает их как "c-N-c-N" (Е-2-е-4 etc.),
    и эта функция служит обработчиком таких сообщений, разделяя клетки хода и приводя их в формат "cN".
    """
    new_strings = []
    for string in strings:
        if string.count('-') == 3:  # "c-N-c-N"
            c1, n1, c2, n2 = string.split('-')
            new_strings.extend((c1 + n1, c2 + n2))
        elif string.count('-') == 2:  # "c-N c-N", не видел такого
            m1, m2 = string.split()
            c1, n1 = m1.split('-')
            c2, n2 = m2.split('-')
            new_strings.extend((c1 + n1, c2 + n2))
        elif string.count('-') == 1:  # "c-N"
            new_strings.append(''.join(string.split('-')))
        else:
            new_strings.append(string)

    return new_strings


def ru_to_eng(string: str):
    """
    Перевод русских буковок в английские, чтоб ход понятно было что и кто.
    """
    string = string.replace('джи', 'g').replace('аш', 'h')
    new_string = str.translate(string, str.maketrans('абсцдефгжхи', 'abccdefgghe'))
    return new_string


def get_config(
        message: str,
        tts: str,
        buttons: list[str] | None,
        card: dict[str, str] | None,
        session_state: dict[str, Any]
):
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons or list(),
        'card': card or dict(),
        'session_state': session_state
    }


def handler_not_a_move(event) -> dict | None | str:
    """
    Обработчик на тот случай, если в сообщении не было найдено ходов.
    Может быть, пользователь попросил помощи или правила?
    """
    lang = getLanguage(event)
    command = event["request"]["command"] + ' ' + event["request"]["original_utterance"]
    if 'правила' in command.lower() or 'rules' in command.lower():
        return getHelpConfig(lang)
    return None


def get_next_move(user_move: str, orientation: str, prev_moves: str, lang: str, session_states) -> dict:
    # Часть запроса к движку за ходом
    if not prev_moves and orientation == 'b':
        user_move = None
    params = {
        "user_move": user_move,
        "prev_moves": prev_moves,
        "orientation": orientation,
        "skill_level": 10,  # session_states.get("skill_level")  Сделать выбор уровня сложности???
        "ram_hash": 128,
        "depth": 15,
        "max_time": 350  # Для ускорения апи, минимум в константах, ищите в кода апи
    }

    response = requests.get(api_base + 'move', params)
    if not response:
        message = game[lang]['error'](response.json()["message"])
        tts = game[lang]['error_tts']
        buttons = messages[lang]["buttons"]
        return get_config(message, tts, buttons, None, session_states)

    return response.json()["response"]


def pre_handle_move(event):
    lang = getLanguage(event)
    tokens = [ru_to_eng(str(s).lower()) for s in event["request"]["nlu"]["tokens"]]
    move = ''.join([token for token in tokens if token in 'abcdefgh12345678'])

    try:
        prev_moves = getState(event, 'prev_moves')
    except KeyError:
        prev_moves = ''

    session_states = {
        "branch": "chessGame",
        "orientation": getState(event, 'orientation'),
        "prev_moves": prev_moves,
    }

    if session_states["orientation"] == "b" and not session_states["prev_moves"]:
        pass  # cringe of project
    elif not is_move(move):
        if answer_config := handler_not_a_move(event):
            return answer_config
        message = game[lang]["unknown_move"](event["request"]["command"])
        tts = game[lang]["unknown_move_tts"]
        buttons = messages[lang]["buttons"]
        return get_config(message, tts, buttons, None, session_states)
    return move, session_states


def event_move(event):
    values = pre_handle_move(event)
    if isinstance(values, dict):
        return values
    move, session_states = values
    lang = getLanguage(event)
    orientation = getState(event, 'orientation')
    data = get_next_move(move, orientation, session_states["prev_moves"], lang, session_states)
    if 'tts' in data:  # Если словарь с tts - это результат get_config
        return data

    stockfish_move = data["stockfish_move"]
    board_id = get_board_id(data["fen"], session_states["orientation"], data["stockfish_move"], data["check"])
    if not board_id:
        message = game[lang]["board_image_error"]
        tts = game[lang]["board_image_error_tts"]
        buttons = messages[lang]["buttons"]
        return get_config(message, tts, buttons, None, session_states)
    card = {
        "type": "BigImage",
        "image_id": board_id,
    }

    if data['end_type'] is not None:
        if data["end_type"] is not None:
            who_win = 'w' if data["orientation"] == 'b' else 'b'
        else:
            who_win = None

        if who_win == "w":
            message = game[lang]['end_game']['white']
        elif who_win == "b":
            message = game[lang]['end_game']['black']
        else:
            message = game[lang]['end_game']['draw']
        card['title'] = message
        del session_states["prev_moves"]
        del session_states["orientation"]
    else:
        message = game[lang]["skill_do_move"](stockfish_move, 'тебе шах' if data['check'] else '')
        session_states["prev_moves"] = data["prev_moves"]

    tts = message
    buttons = messages[lang]["buttons"]
    return get_config(message, tts, buttons, card, session_states)
