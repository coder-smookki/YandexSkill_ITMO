message = \
    """
    Вы направились в категорию "Учебные издания". Скажите или напишите издание, которое вы хотите найти.
    """

tts = \
    """
    Вы направились в категорию "Учебные издания". Скажите или напишите издание, которое вы хотите найти.
    """

buttons = [
    "Повторить еще раз",
    "Что ты умеешь?",
    "Помощь",
    "Назад",
    "Выйти"
]

card = {
    'type': 'BigImage',
    'image_id': '997614/e38bbfd1a2235c7229b1',
    'title': 'УЧЕБНЫЕ ИЗДАНИЯ',
    'description': \
        """
        Напишите или скажите издание, которое вы хотите найти.
        """
}

session_state = {
    "branch": "educationalPublications"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
