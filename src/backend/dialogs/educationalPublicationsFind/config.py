from utils.parser.parser import *

buttons = [
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"  
]

session_state = {
    "branch": "educationalPublications"
}

def getConfig(event):
    message = ''
    tts = ''

    announces = parser('educationalPublications', event["request"]['command'])[:6]

    for i in announces:
        message += f"""
        {i['title']}\n
        {i['text']}\n
        {i['link']}\n
        ------------\n
        """
        tts += f'{i["title"]}'

    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }
