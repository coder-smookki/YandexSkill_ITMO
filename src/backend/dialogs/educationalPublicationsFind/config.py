from utils.parser.parser import *
from utils.responseHelper import getLanguage
import copy



def getConfig(event):
    session_state = {"branch": "educationalPublications"}
    words = {
        "ru-RU": {
            "buttons": [
                "Повторить еще раз",
                "Что ты умеешь?",
                "Помощь",
                "Назад",
                "Выйти",
            ],
            "tts": "Учебные издания:\n",
        },
        "en-US": {
            "buttons": [
                "Say it again",
                "What can you do?",
                "Help",
                "Back",
                "Exit",
            ],
            "tts": "Educational Editions:\n",
        },
    }

    lang = getLanguage(event)

    message = ""
    tts = words[lang]["tts"]
    buttons = words[lang]["buttons"]

    publications = parser("educationalPublications", event["request"]["command"])

    for i in range(len(publications)):
        message += f"""{publications[i]['title']}\n------------\n"""
        tts += f'{publications[i]["title"]}'
        buttons.append(
            {
                "title": f"{publications[i]['title']}",
                "url": f"{publications[i]['link']}",
                "hide": False,
            }
        )

    buttons_response = copy.deepcopy(buttons)

    buttons.clear()

    return {
        "message": message,
        "tts": tts,
        "buttons": buttons_response,
        "session_state": session_state,
    }
