from utils.globalStorage import globalStorage

def getConfig():
    message = 'Вы направились в категорию "Контесты.\n'

    tts = 'Контесты. '

    buttons = [
        "Повторить ещё раз",
        "Помощь",
        "Назад",
        "Выйти"
    ]

    session_state = {
        "branch": "contests"
    }

    contests = globalStorage['news_contests']

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