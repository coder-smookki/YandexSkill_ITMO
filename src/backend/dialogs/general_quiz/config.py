from src.backend.utils.quiz.questions import *

quest = answer_question()

message = \
    f"""
    {quest[0]}
    """

tts = \
    """
    Вы направились в категорию "Квесты". Вы можете начать викторину по нажатию кнопки - Начать. При взаимодействие с кнопкой, будут запущены вопросы на которые вы должны дать правильные ответы. Вы готовы к викторине?
    """

buttons = [
    "Начать",
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
        """
        Вы готовы начать викторину? Чтобы начать, нажмите на кнопку "Начать".
        """
}

session_state = {
    "branch": "start_quiz"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }


print(getConfig())
