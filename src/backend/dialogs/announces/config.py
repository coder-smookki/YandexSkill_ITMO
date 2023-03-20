from utils.globalStorage import globalStorage
from utils.responseHelper import getLanguage


def getConfig(event):
    words = {
        "ru-RU": {
            "message": "Анонсы:\n",
            "tts": "Анонсы:\n",
            "buttons": [
                "Повторить ещё раз",
                "Что ты умеешь?",
                "Помощь",
                "Назад",
                "Выйти",
            ],
            "emptyArr": "К сожалению, анонсов сейчас нет.",
            "annBetween": ". будет ",
        },
        "en-US": {
            "message": "Announcements:\n",
            "tts": "Announcements:\n",
            "buttons": [
                "Say it again",
                "What can you do?",
                "Help",
                "Back",
                "Exit",
            ],
            "emptyArr": "Unfortunately, there are no announcements at the moment..",
            "annBetween": ". will be on ",
        },
    }

    lang = getLanguage(event)

    message = words[lang]["message"]
    tts = words[lang]["tts"]
    buttons = words[lang]["buttons"]
    emptyArr = words[lang]["emptyArr"]
    annBetween = words[lang]["annBetween"]

    session_state = {"branch": "announces"}
    announces = globalStorage["news_announces_" + lang]

    buttonsResponse = []
    if len(announces) <= 0:
        message = emptyArr
        tts = emptyArr
    else:
        for i in announces:
            message += f"""
            {i['text']}\n
            {i['date']}\n
            ------------\n
            """
            buttonsResponse.append({"title": i["text"], "url": i["link"]})
            tts += f'{i["text"]}{annBetween}{i["date"]}.'

        buttons = buttonsResponse + buttons

    return {
        "message": message,
        "tts": tts,
        "buttons": buttons,
        "session_state": session_state,
    }
