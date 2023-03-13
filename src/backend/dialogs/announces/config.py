from parser.parser import *

message = ''

tts = ''

announces = parser('announces')
 
for i in announces:
    message += f"""
    {i['text']}\n
    {i['link']}\n
    {i['date']}\n
    ------------\n
    """
    tts += f'{i["text"]} будет {i["date"]} '

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

session_state = {
    "branch": "news"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }