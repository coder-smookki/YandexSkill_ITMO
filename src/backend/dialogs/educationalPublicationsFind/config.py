from utils.parser.parser import *

message = ''
tts = ''

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

session_state = {
    "branch": "educationalPublications"
}

def getConfig(event):
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }