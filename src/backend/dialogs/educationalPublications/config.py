message = \
    """
    Вы направились в категорию "Учебные издания"

    """

tts = \
    """
    Вы направились в категорию "Учебные издания"
    Что вы хотите найти?
    """

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'УЧЕБНЫЕ ИЗДАНИИЯ',
    'description': \
        """
        Вы направились в категорию "Учебные издания"
        Напишите, что вам нужно найти в учебных изданиях
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
