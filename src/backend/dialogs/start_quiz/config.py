tts = \
    """
    Вы перешли в категорию "Начало Викторины". 
    Вы можете начать викторину по нажатию кнопки - Начать.
    При запуске викторины, будут запущены вопросы. На которые вы должны дать правильные ответы.
    Один правильный ответ, равняется одному баллу.
    Вы готовы к викторине?    
    """

buttons = [
    "Начать",
    "Повторить ещё раз",
    'Что ты умеешь?',
    "Помощь",
    "Назад",
    "Выйти"

]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'НАЧАЛО ВИКТОРИНЫ',
    'description': \
        """
        Вы готовы начать викторину?
        """
}

session_state = {
    "branch": "start_quiz",
    "count_questions": 0,
    "count_correct_response": 0,
    "questions_list": []
}


def getConfig():
    return {
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
