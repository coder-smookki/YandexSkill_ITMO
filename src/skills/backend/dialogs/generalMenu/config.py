message=\
"""
Привет Студент! Чтобы пользоваться навыком, выбери язык.
Hello Student! To use the skill, choose a language.
    1. Русский Язык (Russian Language)
    2. Английский Язык (English Language)
"""

tts=\
"""
Привет Студент! Чтобы пользоваться навыком, выбери язык.
Hello Student! To use the skill, choose a language.
    Первое - это Русский Язык
    The first is the Russian Language
    Второе - это Английский Язык
    The second is English
"""

buttons=[
    "Русский Язык (Russian Language)",
    "Английский язык (English Language)"
]

card={
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ГЛАВНОЕ МЕНЮ (GENERAL MENU)',
    'description':\
        """
        Первое (first) - Рус. Язык (Russian Language)... Второе (second) - Англ. Язык (English Language)...
        """
}

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card
    }


