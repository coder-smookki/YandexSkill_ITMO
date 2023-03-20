from utils.globalStorage import globalStorage
from utils.responseHelper import getLanguage
# news_contests
# for i in contests:
#             message += f"""
#             {i['text']}\n
#             {i['link']}\n
#             {i['date']}\n
#             ------------\n
#             """
#             tts += f'{i["text"]} будет {i["date"]}.'

def getConfig(event):
    words = {
        "ru-RU": {
            "message": "Контесты:\n",
            "tts": "Контесты:\n",
            "buttons": [
                "Повторить ещё раз",
                "Что ты умеешь?",
                "Помощь",
                "Назад",
                "Выйти",
            ],
            "emptyArr": "К сожалению, контестов сейчас нет.",
            "annBetween": ". будет ",
        },
        "en-US": {
            "message": "Contests:\n",
            "tts": "Contests:\n",
            "buttons": [
                "Say it again",
                "What can you do?",
                "Help",
                "Back",
                "Exit",
            ],
            "emptyArr": "Unfortunately, there are no contests at the moment..",
            "annBetween": ". will be on ",
        },
    }

    lang = getLanguage(event)

    message = words[lang]["message"]
    tts = words[lang]["tts"]
    buttons = words[lang]["buttons"]
    emptyArr = words[lang]["emptyArr"]
    annBetween = words[lang]["annBetween"]

    session_state = {"branch": "contests"}
    contests = globalStorage["news_contests_" + lang]

    buttonsResponse = []
    if len(contests) <= 0:
        message = emptyArr
        tts = emptyArr
    else:
        for i in contests:
            message += f"""
            {i['text']}\n
            {i['link']}\n
            {i['date']}\n
            ------------\n
            """
            buttonsResponse.append({"title": i["text"], "url": i["link"]})
            tts += f'{i["text"]}{annBetween}{i["date"]}.'


    return {
        "message": message,
        "tts": tts,
        "buttons": buttons,
        "session_state": session_state,
    }
