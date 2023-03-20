from utils.globalStorage import globalStorage


def getConfig():
    message = 'Контесты:\n'

    tts = 'Контесты:\n'

    buttons = [
        "Повторить ещё раз",
        "Что ты умеешь?",
        "Помощь",
        "Назад",
        "Выйти"
    ]

    session_state = {
        "branch": "contests"
    }

    contests = globalStorage['news_contests']

    if len(contests) <= 0:
        message = 'К сожалению, контестов сейчас нет.'
        tts = 'К сожалению, контестов сейчас нет'
    else:
        for i in contests:
            message += f"""
            {i['text']}\n
            {i['link']}\n
            {i['date']}\n
            ------------\n
            """
            tts += f'{i["text"]} будет {i["date"]}. '

    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }
