from utils.parser.parser import *

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

session_state = {
    "branch": "educationalPublications"
}

def getConfig(event):
    message = ''
    tts = ''

    announces = parser('educationalPublications', event['request']['original_utterance'])

    for i in announces:
        message += f"""
        {i['title']}\n
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