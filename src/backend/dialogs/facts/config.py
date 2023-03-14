import csv
import random

# Открываем CSV файл для чтения
with open('facts.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)
    values = [row[0] for row in reader]
    random_value = random.choice(values)

message = \
    f"""
    {random_value}
    """

tts = \
    f"""
    {random_value}
    """

buttons = [
    "Начать",
    "Следующий факт",
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"

]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ВИКТОРИНА',
    'description': \
        f"""
        {random_value}
        """
}

session_state = {
    "branch": "facts"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }