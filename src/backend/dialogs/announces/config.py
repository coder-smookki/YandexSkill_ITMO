from utils.globalStorage import globalStorage


def getConfig(lang='ru'):
    message = 'Анонсы:\n'

    tts = 'Анонсы:\n'

    buttons = [
        "Повторить ещё раз",
        "Что ты умеешь?",
        "Помощь",
        "Назад",
        "Выйти"
    ]

    session_state = {
        "branch": "announces"
    }

    announces = globalStorage['news_announces']
    buttonsResponse = []
    if len(announces) <= 0:
        message = 'К сожалению, анонсов сейчас нет.'
        tts = 'К сожалению, анонсов сейчас нет.'
    else:
        for i in announces:
            message += f"""
            {i['text']}\n
            {i['date']}\n
            ------------\n
            """
            buttonsResponse.append({'title': i['text'], 'url': i['link']})
            tts += f'{i["text"]}. будет {i["date"]}.'

        buttons = buttonsResponse + buttons

    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }
