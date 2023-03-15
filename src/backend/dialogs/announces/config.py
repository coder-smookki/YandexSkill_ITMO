from utils.parser.parser import *

message = ''

tts = ''

announces = parser('announces')
 
for i in announces:
    message += f"""
    {i['text']}.\n
    {i['link']}.\n
    {i['date']}.\n
    ------------\n
    """
    tts += f'Вы направились в категорию "Анонсы". {i["text"]} будет {i["date"]} '

buttons = [
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"  
]

session_state = {
    "branch": "announces"
}

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }
