message = \
    """
    Вопрос:
    Как подать заявку на получение документа о предыдущем образовании?
    
    Ответ:
    Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
    """

tts = \
    """
    Вы направились в категорию "Как подать заявку на получение документа о предыдущем образование?" Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
    """

buttons = [
    "Повторить ещё раз",
    "Что ты умеешь?",
    "Помощь",
    "Назад",
    "Выйти"
]
card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'ДОКУМЕНТ О ПРЕДЫДУЩЕМ ОБРАЗОВАНИИ',
    'description': \
        """
        Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
        """
}

session_state = {
    "branch": "documentOnPreviousEducation"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
