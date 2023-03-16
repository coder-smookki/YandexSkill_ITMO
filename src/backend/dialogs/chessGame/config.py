choose_color_message = \
    """
    За какой цвет будете играть? Белый или чёрный?
    """
choose_color_tts = choose_color_message

user_move_first_message = \
    """
    Вы играете белыми! Называйте, откуда и куда?
    """
user_move_first_tts = user_move_first_message
user_move_first_card = {
    'type': 'BigImage',
    'image_id': {},  # Айди картинки начальной позиции, сделать
    'title': 'Начальная позиция за белых',
}

buttons = [
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
    }


def get_config_user_move_first():
    return {
        'message': user_move_first_message,
        'tts': user_move_first_tts,
        'buttons': buttons,
        'card': user_move_first_card,
    }
