ru_choose_color_message = ru_choose_color_tts = """За какой цвет будете играть? Белый или чёрный?"""

ru_user_move_first_message = ru_user_move_first_tts = """Вы играете белыми! Называйте, откуда и куда?"""

ru_user_move_first_card = {
    'type': 'BigImage',
    'image_id': '1540737/d363e07d1d626e9cfca7',  # Айди картинки начальной позиции
    'title': 'Ваш ход!',
}

ru_user_move_second_message = ru_user_move_second_tts = """Вы играете черными! Скажите мне что-то, чтобы я сделал первый ход."""

ru_choose_color_buttons = [
    'Белый',
    'Черный',
    "Правила",
    "Назад",
    "Выйти",
    "Помощь",
]

ru_buttons = [
    "Правила",
    "Назад",
    "Выйти",
    "Помощь",
]

eng_choose_color_message = eng_choose_color_tts = """What color will you play for? White or black?"""

eng_user_move_first_message = eng_user_move_first_tts = """You're playing white! Tell me where from and where to?"""

eng_user_move_second_message = eng_user_move_second_tts = """You're playing black! Say something so that I make the first move for white."""

eng_user_move_first_card = {
    'type': 'BigImage',
    'image_id': '1540737/d363e07d1d626e9cfca7',  # Айди картинки начальной позиции
    'title': 'Your turn!',
}

eng_choose_color_buttons = [
    'White',
    'Black',
    "Rules",
    "Help",
    "Back",
    "Exit",
]

eng_buttons = [
    "Rules",
    "Help",
    "Back",
    "Exit",
]

messages = {
    "ru-RU": {
        "user_choose_color_message": ru_choose_color_message,
        "user_choose_color_tts": ru_choose_color_tts,
        "user_move_first_message": ru_user_move_first_message,
        "user_move_first_tts": ru_user_move_first_tts,
        "user_move_second_message": ru_user_move_second_message,
        "user_move_second_tts": ru_user_move_second_tts,
        "user_move_first_card": ru_user_move_first_card,
        "user_choose_color_buttons": ru_choose_color_buttons,
        "buttons": ru_buttons
    },
    "en-US": {
        "user_choose_color_message": eng_choose_color_message,
        "user_choose_color_tts": eng_choose_color_tts,
        "user_move_first_message": eng_user_move_first_message,
        "user_move_first_tts": eng_user_move_first_tts,
        "user_move_second_message": eng_user_move_second_message,
        "user_move_second_tts": eng_user_move_second_tts,
        "user_move_first_card": eng_user_move_first_card,
        "user_choose_color_buttons": eng_choose_color_buttons,
        "buttons": eng_buttons
    }
}

game = {
    "ru-RU": {
        "error": "Возникла ошибка {}, попробуйте ещё раз."
                 '\nСкажите "Правила", если снова не получится'.format,
        "error_tts": "Возникла ошибка, попробуйте ещё раз."
                     '\nСкажите "Правила", если снова не получится',
        "illegal_move_tts": "{} - невозможный ход, попробуйте ещё раз."
                            '\nСкажите "Правила", если снова не получится'.format,
        "unknown_move": 'Не удалось распознать ход в фразе "{}", попробуйте ещё раз.'
                        '\nСкажите "Правила", если снова не получится'.format,
        "unknown_move_tts": f'Не удалось распознать ход, попробуйте ещё раз'
                            f'\nСкажите "Правила", если снова не получится',
        "board_image_error": "Ошибка на сервере с получением картинки.",
        "board_image_error_tts": "Ошибка на сервере с получением картинки.",
        "end_game": {
            "white": "Игра закончилась победой белых!",
            "black": "Игра закончилась победой чёрных!",
            "draw": "Игра закончилась в ничью..."
        },
        "skill_do_move": 'Я сходил на "{}" {}, {}.'.format,
        "check": "тебе шах!"
    },
    "en-US": {
        "error": "An error occurred - {}, try again."
                 '\nSay "Rules" if it doesnt work out again'.format,
        "error_tts": "An error occurred, try again."
                     '\nSay "Rules" if it doesnt work out again.',
        "illegal_move_tts": "{} - illegal move, try again."
                            '\nSay "Rules" if it doesnt work out again.'.format,
        "unknown_move": 'Failed to recognize the move in the phrase "{}", try again.'
                        '\nSay "Rules" if it doesnt work out again'.format,
        "unknown_move_tts": f'Failed to recognize the move, try again'
                            f'\nSay "Rules" if it doesnt work out again',
        "board_image_error": "Error on the server with receiving the image.",
        "board_image_error_tts": "Error on the server with receiving the image.",
        "end_game": {
            "white": "The game ended with White winning!",
            "black": "The game ended with Black winning!",
            "draw": "The game ended in a draw..."
        },
        "skill_do_move": 'I made a move on "{}" {}, {}}.'.format,
        "check": "check!"

    }
}

your_turn = {
    "ru-RU":
        ['твой ход',
         'твоя очередь',
         'теперь твой ход',
         'теперь твоя очередь',
         'теперь ходи ты',
         'давай, ходи',
         'я жду твоего хода',
         'Я сходил, теперь ты',
         'Ты можешь начинать ходить',
         'Говори, откуда и куда',],
    "en-US":
        ['your move',
         'your turn',
         'now its your turn',
         'now its your move',
         'les go, move',
         'come on, les go',
         'im waiting for your move',
         'I made a move, now you',
         'You can make a move',
         'Say, from which cell to which'],
}


def get_config_choose_color(lang: str):
    return {
        'message': messages[lang]["user_choose_color_message"],
        'tts': messages[lang]["user_choose_color_tts"],
        'buttons': messages[lang]["user_choose_color_buttons"],
        'session_state': {
            "branch": "chessGame"
        }
    }


def get_config_user_move_first(lang: str):
    return {
        'message': messages[lang]["user_move_first_message"],
        'tts': messages[lang]["user_move_first_tts"],
        'buttons': messages[lang]["buttons"],
        'card': messages[lang]["user_move_first_card"],
        'session_state': {
            "branch": "chessGame",
            "orientation": "w"
        }
    }


def get_config_user_move_second(lang: str):
    return {
        'message': messages[lang]["user_move_second_message"],
        'tts': messages[lang]["user_move_second_tts"],
        'buttons': messages[lang]["buttons"],
        'session_state': {
            "branch": "chessGame",
            "orientation": "b"
        }
    }
