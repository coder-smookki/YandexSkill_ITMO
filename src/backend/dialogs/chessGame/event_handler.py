import os
from typing import Any
from itertools import product

from dotenv import load_dotenv;

load_dotenv()  # noqa
import requests

from src.backend.dialogs.chessMain import config

oauth_key = os.environ["OAUTH_IMAGE_KEY"]
skill_id = os.environ["SKILL_ID"]

# Изменить на 127.0.0.1, если будем запускать в ВМ Швепса
api_base = 'http://46.39.30.114:5000/api/chess/'

all_squares = {f'{c}{n}' for c, n in product('abcdefhg', '12345678')}
ask_help = 'Скажите "Помощь", если не получится ещё раз.'


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
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }


def handler_not_a_move(event) -> dict | None:
    """
    Обработчик на тот случай, если в сообщении не было найдено ходов.
    Может быть, пользователь попросил помощи или правила?
    """
    command = event["request"]["command"] + ' ' + event["request"]["original_utterance"]
    if 'помощь' in command.lower() or 'правила' in command.lower():
        event["session"]["state"]["branch"] = "chessMain"
        return get_config(
            config.rules,
            config.rules_tts,
            config.buttons,
            None,
            event["session"]["state"]["branch"]
        )
    return None


def get_next_move(user_move: str, session_states: dict[str, Any]) -> dict:
    # Часть запроса к движку за ходом
    params = {
        "user_move": user_move,
        "prev_moves": session_states.get("prev_moves"),
        "orientation": session_states.get("orientation"),
        "skill_level": 1,  # session_states.get("skill_level")  Сделать выбор уровня сложности???
        "ram_hash": 1,  # Для ускорения апи, минимум в константах, ищите в кода апи
        "depth": 1,  # Для ускорения апи, минимум в константах, ищите в кода апи
    }

    response = requests.get(api_base + 'move', params)
    if response.status_code != 200:
        message = f'Возникла ошибка "{response.json()["message"]}", попробуйте ещё раз. ' + ask_help
        tts = f'Возникла ошибка на сервере, попробуйте ещё раз' + ask_help
        return get_config(
            message,
            tts,
            config.buttons,
            None,  # Как получить прошлую картинку?
            session_states
        )

    return response.json()


def get_bigimage_board(last_move: str, fen: str, session_states: dict) -> dict | None:
    params = {
        "last_move": last_move,
        "fen": fen
    }
    board_response = requests.get(api_base + 'board', params=params)
    if board_response != 200:  # Либо сервер сломался, либо неверные параметры в ходе игры.
        message = f'Возникла ошибка "{board_response.json().get("message")}", попробуйте ещё раз. ' + ask_help
        tts = f'Возникла ошибка на сервере, попробуйте ещё раз' + ask_help
        return get_config(
            message,
            tts,
            config.buttons,
            None,  # Как получить прошлую картинку?
            session_states
        )

    data = {
        "Host": "https://dialogs.yandex.net",
        "Authorization": f'OAuth {oauth_key}',
        "Content-Type": "multipart/form-data"
    }
    # !!! Я не уверен в правильности форматов data и самого запроса!!!
    yandex_response = requests.post(data["Host"] + f'/api/v1/skills/{skill_id}/images',
                                    data=data, files=board_response.content)
    if yandex_response.status_code == 429:  # Обработка момента, когда занята вся память навыка (около 2к картинок)
        pass

    if yandex_response.status_code != 200:
        message = f'Возникла ошибка "{yandex_response.json()["message"]}", попробуйте ещё раз. ' + ask_help
        tts = f'Возникла ошибка на сервере, попробуйте ещё раз' + ask_help
        return get_config(
            message,
            tts,
            config.buttons,
            None,  # Как получить прошлую картинку?
            session_states
        )

    card = {
        "type": "BigImage",
        "image_id": yandex_response.json()["image"]["id"],
        "title": "",  # Нужен ли заголовок? Можно сделать пустым?
        "description": "",  # Нужно ли описание? Можно сделать пустым?
        "button": {
            "text": "Надпись на кнопке",
            "url": f"https://lichess.org/analysis/fromPosition/{fen}",
            "payload": {}
        }
    }

    return card


def get_position_score(prev_moves: str, session_states: dict) -> dict | None:
    params = {
        "prev_moves": prev_moves
    }
    response = requests.get(api_base + 'position', params=params)
    if response != 200:  # Либо сервер сломался, либо неверные параметры в ходе игры.
        message = f'Возникла ошибка "{response.json()["message"]}", попробуйте ещё раз. ' + ask_help
        tts = f'Возникла ошибка на сервере, попробуйте ещё раз' + ask_help
        return get_config(
            message,
            tts,
            config.buttons,
            None,  # Как получить прошлую картинку?
            session_states
        )

    return response.json()


def event_handler(event):
    # Часть обработки сообщения пользователя
    tokens = replace_scores_to_spaces([ru_to_eng(s.lower()) for s in event["request"]["nlu"]["tokens"]])
    moves = [token for token in tokens if token in all_squares]
    session_states = event["session"]["state"]

    if len(moves) != 2:
        if answer_config := handler_not_a_move(event):
            return answer_config
        message = f'Не удалось распознать ход в фразе "{event["request"]}", попробуйте ещё раз. ' + ask_help
        tts = f'Не удалось распознать ход, попробуйте ещё раз. ' + ask_help
        return get_config(
            message,
            tts,
            config.buttons,
            None,  # Как получить прошлую картинку?
            session_states
        )

    data = get_next_move(''.join(moves), session_states)
    if 'tts' in data:  # Если словарь с tts - это результат get_config
        return data

    stockfish_move = data["stockfish_move"]
    card = get_bigimage_board(stockfish_move, data["fen"], session_states)
    if isinstance(card, dict) and 'tts' in card:
        return card  # Если словарь с tts - это результат get_config

    score = get_position_score(data["prev_moves"], session_states)
    if 'tts' in data:  # Если словарь с tts - это результат get_config
        return data

    if score['is_end']:
        session_states["branch"] = 'chessMain'
        message = 'Игра закончилась '
        if score["who_win"] == "w":
            message += 'победой белых!'
        elif score["who_win"] == "b":
            message += 'победой чёрных!'
        else:
            message += 'патом...'
    else:
        message = f'Я сходил на "{stockfish_move}", теперь ваш ход.'
    tts = message

    session_states["prev_moves"] = data["prev_moves"]
    return get_config(message, tts, config.buttons, card, session_states)
