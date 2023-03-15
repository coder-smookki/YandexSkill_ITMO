from utils.parser.parser import *

buttons = [
    "Назад",
    "Выйти",
    "Помощь",
    {
        "title": 'Кнопка для теста',
        "url": 'https://www.youtube.com/watch?v=Zb0WTZ--nbc',
        "hide": False
    }
]

session_state = {
    "branch": "educationalPublications"
}

def getConfig(event):
    message = ''
    tts = ''

    announces = parser('educationalPublications', event['request']['original_utterance'])

    for i in range(len(announces)):
        message += f"""
        {announces[i]['title']}\n
        ------------\n
        """
        tts += f'{announces[i]["title"]}'
        buttons.append({"title": 'Типа название кнопки', "url": f"{announces[i]['link']}", "hide": False})

    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }