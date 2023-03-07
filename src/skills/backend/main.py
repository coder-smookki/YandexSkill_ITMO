from src.skills.backend.backend import *


# def handler(event, context):
#    """
#    Точка входа для облачной функции.
#    :param event: содержимое request.json().
#    :param context: информация о текущем контексте выполнения.
#    :return: ответ будет представлен в виде json автоматически.
#    """
#    text = 'Привет, я повторю все, что вы скажете'
#    if 'request' in event and \
#            'original_utterance' in event['request'] \
#           and len(event['request']['original_utterance']) > 0:
#        text = event['request']['original_utterance']
#    return {
#        'version': event['version'],
#        'session': event['session'],
#        'response': {
#            'text': text,
#            'end_session': 'false'
#        },
#    }

def main(event, context):
    """
    Точка входа для облачной функции.
    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    if event['session']['new'] == 'true':
        return general_menu(event, context)
    if event['session']['new'] == 'false':
        pass


def general_menu(event, context):
    """
    Точка входа для облачной функции.
    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        'suggests': [
            'Русский Язык (Russian Language)',
            'Английский язык (English Language)',
            'Выйти (Exit)',
            'Помощь (Help)'
        ]
    }
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text':
                """
Привет Студент! Чтобы пользоваться навыком, выбери язык.

Hello Student! To use the skill, choose a language.

       1. Русский Язык (Russian Language)
       2. Английский Язык (English Language)
                """,
            'tts':
                """
Привет Студент! Чтобы пользоваться навыком, выбери язык.
Hello Student! To use the skill, choose a language.
       Первое - это Русский Язык (Russian Language)
       Второе - это Английский Язык (English Language)
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'Главное меню (General menu)',
                'description':
                    """
Привет Студент! Чтобы пользоваться навыком, выбери язык.
Hello Student! To use the skill, choose a language.
1 - Русский Язык (Russian Language).
2 - Английский Язык (English Language).
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        }
    }
