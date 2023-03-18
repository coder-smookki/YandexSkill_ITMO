message = \
    """
    Привет Студент! Чтобы пользоваться навыком, выбери язык.
    Hello Student! To use the skill, choose a language.
        1. Русский Язык (Russian Language)
        2. Английский Язык (English Language)
    """

tts = \
    """ 
    Вы перешли в категорию "Главное меню".
    You have moved to the "Main Menu" category.
    Привет Студент! Чтобы пользоваться навыком, выбери язык.
    Hello Student! To use the skill, choose a language.
        Первое - это Русский Язык
        The first is the Russian Language
        Второе - это Английский Язык
        The second is English
    """

buttons = [
    "Русский Язык (Russian Language)",
    "Английский Язык (English Language)"
]

card = {
    'type': 'BigImage',
    'image_id': '1540737/07a6bc185a8dcec1b266',
    'title': 'ГЛАВНОЕ МЕНЮ (GENERAL MENU)',
    'description': \
        """
        Выберите язык - Русский или Английский...
        Select language - Russian or English...
        """
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        "user_state_update": {
            "value": 'someValue'
        },
    }
