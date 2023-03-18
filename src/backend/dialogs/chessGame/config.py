choose_color_message = """
За какой цвет будете играть? Белый или чёрный?
"""
choose_color_tts = choose_color_message

user_move_first_message = """
Вы играете белыми! Называйте, откуда и куда?
"""
user_move_first_tts = user_move_first_message
user_move_first_card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',  # Айди картинки начальной позиции, сделать
    'title': 'Начальная позиция за белых',
}

user_move_second_message = """
Вы играете черными! Скажите мне что-то, чтобы я сделал первый ход.
"""
user_move_second_tts = user_move_first_message

buttons = [
    'Что-то',
    "Назад",
    "Выйти",
    "Помощь",
    "Правила"
]

choose_color_buttons = [
    'Белый',
    'Черный',
    "Назад",
    "Выйти",
    "Помощь",
    "Правила"
]


def get_config_choose_color():
    return {
        'message': choose_color_message,
        'tts': choose_color_tts,
        'buttons': choose_color_buttons,
        'session_state': {
            "branch": "chessGame"
        }
    }


def get_config_user_move_first():
    return {
        'message': user_move_first_message,
        'tts': user_move_first_tts,
        'buttons': buttons,
        'card': user_move_first_card,
        'session_state': {
            "branch": "chessGame",
            "orientation": "w"
        }
    }


def get_config_user_move_second():
    return {
        'message': user_move_second_message,
        'tts': user_move_first_tts,
        'buttons': buttons,
        'card': None,
        'session_state': {
            "branch": "chessGame",
            "orientation": "b"
        }
    }
