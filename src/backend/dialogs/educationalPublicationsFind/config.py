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
    print(event)
    # announces = parser('educationalPublications', event['request']['original_utterance'])

    publications = parser('educationalPublications', event['request']['command'])

    for i in range(len(publications)):
        message += f"""{publications[i]['title']}\n------------\n"""
        tts += f'{publications[i]["title"]}'
        buttons.insert(0, {"title": f'{i+1}', "url": f"{publications[i]['link']}", "hide": False})

    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }