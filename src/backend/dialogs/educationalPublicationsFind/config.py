from utils.parser.parser import *
import copy

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

    publications = parser('educationalPublications', event['request']['command'])

    for i in range(len(publications)):
        message += f"""{publications[i]['title']}\n------------\n"""
        tts += f'{publications[i]["title"]}'
        buttons.append({"title": f"{publications[i]['title']}", "url": f"{publications[i]['link']}", "hide": False})

    buttons_response = copy.deepcopy(buttons)

    buttons.clear()

    return {
        'message': message,
        'tts': tts,
        'buttons': buttons_response,
        'session_state': session_state
    }
