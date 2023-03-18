from typing import Any
from itertools import product
import requests
from dialogs.chessMain import config
from utils.responseHelper import getState
from .db import get_board_id

# Изменить на 127.0.0.1, если будем запускать в ВМ Швепса
api_base = 'http://127.0.0.1:5000/api/chess/'

all_squares = {f'{c}{n}' for c, n in product('abcdefhg', '12345678')}
ask_help = 'Скажите "Помощь", если не получится ещё раз.'


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
    new_string = str.translate(string, str.maketrans('абсцдефгжх', 'abccdefggh'))
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


def handler_not_a_move(event, session_states) -> dict | None:
    """
    Обработчик на тот случай, если в сообщении не было найдено ходов.
    Может быть, пользователь попросил помощи или правила?
    """
    command = event["request"]["command"] + ' ' + event["request"]["original_utterance"]
    if 'помощь' in command.lower() or 'правила' in command.lower():
        return get_config(
            config.rules,
            config.rules_tts,
            config.buttons,
            None,
            session_states
        )
    return None


def get_next_move(user_move: str, event, prev_moves: str, session_states) -> dict:
    # Часть запроса к движку за ходом
    params = {
        "user_move": user_move,
        "prev_moves": prev_moves,
        "orientation": getState(event, 'orientation'),
        "skill_level": 1,  # session_states.get("skill_level")  Сделать выбор уровня сложности???
        "ram_hash": 1,  # Для ускорения апи, минимум в константах, ищите в кода апи
        "depth": 1,  # Для ускорения апи, минимум в константах, ищите в кода апи
    }

    response = requests.get(api_base + 'move', params)
    if response.status_code != 200:
        message = f'Возникла ошибка "{response.json()["message"]}", {user_move}, попробуйте ещё раз. ' + ask_help
        tts = f'Возникла ошибка на сервере, попробуйте ещё раз' + ask_help
        return get_config(message, tts, config.buttons, None, session_states)

    return response.json()["response"]


def event_move(event):
    # try:
    #     prev_moves = getState(event, 'prev_moves')
    # except KeyError:
    #     prev_moves = ''
    #
    # session_states = {
    #     "branch": "chessGame",
    #     "orientation": getState(event, 'orientation'),
    #     "prev_moves": prev_moves,
    # }
    #
    # return get_config('Тест', 'Тест', ['1', '2'], None, session_states)
    # Часть обработки сообщения пользователя
    tokens = [ru_to_eng(str(s).lower()) for s in event["request"]["nlu"]["tokens"]]
    move = ''.join([token for token in tokens if token in 'abcdefgh12345678'])
    print(f'{move=}')

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
        pass
    elif not is_move(move):
        if answer_config := handler_not_a_move(event, session_states):
            return answer_config
        message = f'Не удалось распознать ход в фразе "{event["request"]["command"]}", попробуйте ещё раз. ' + ask_help
        tts = f'Не удалось распознать ход, попробуйте ещё раз. ' + ask_help
        return get_config(message, tts, config.buttons, None, session_states)

    data = get_next_move(move, event, session_states["prev_moves"], session_states)
    if 'tts' in data:  # Если словарь с tts - это результат get_config
        print(f'{event["request"]=}\n{tokens=}\n{move=}')
        return data

    stockfish_move = data["stockfish_move"]
    board_id = get_board_id(data["fen"], data["orientation"], data["stockfish_move"], data["check"])
    if not board_id:
        message = f'Ошибка на сервере с получением картинки. ' + ask_help
        tts = f'Ошибка на сервере с получением картинки. ' + ask_help
        return get_config(message, tts, config.buttons, None, session_states)
    card = {
        "type": "BigImage",
        "image_id": board_id,
        "title": "Заголовок",
        "description": "Описание",
        "button": {
            "text": "Кнопка",
            "url": f"https://lichess.org/analysis/fromPosition/" + data["fen"],
        }
    }

    if data['end_type'] is not None:
        del session_states["prev_moves"]

        if data["check"] is not None:
            who_win = 'w' if data["orientation"] == 'b' else 'b'
        else:
            who_win = None

        message = 'Игра закончилась '
        if who_win == "w":
            message += 'победой белых!'
        elif who_win == "b":
            message += 'победой чёрных!'
        else:
            message += 'в ничью...'

        del session_states["orientation"]
    else:
        message = f'Я сходил на "{stockfish_move}", теперь ваш ход.'
        session_states["prev_moves"] = data["prev_moves"]

    tts = message

    return get_config(message, tts, config.buttons, None, session_states)
