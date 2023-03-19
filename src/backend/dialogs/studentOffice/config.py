message = \
    """
    Вы направились в категорию "Студенческий офис"
    
    О нас:
    Каждый день у студента возникает миллион вопросов. Как получить справку? Как заменить студенческий билет?\n
    Возможно ли продлить сессию? На эти и многие другие вопросы знает ответ Студенческий офис.
    
    
    Контакты:
    so@itmo.ru
    +7 (812) 607-04-74
    +7 (812) 480-90-00
    
    Выберите вопрос чтобы получить ответ:
    
    Что такое Студенческий офис?
    Зачем мне обращаться в Студенческий офис?
    Как подать заявку на получение справки/документа о предыдущем образовании?
    Как попасть на консультацию в Студенческий офис?
    Я не знаю, кому задать вопрос. Студенческий офис поможет?
    """

tts = \
    """
    Вы направились в категорию "Студенческий офис"
    О нас:
    Каждый день у студента возникает миллион вопросов. Как получить справку? Как заменить студенческий билет?
    Возможно ли продлить сессию? На эти и многие другие вопросы знает ответ Студенческий офис.
    Контакты:
    Почта - so@itmo.ru
    Телефон - плюс семь, восемьсот двенадцать, шестьсот семь, ноль четыре, семьдесят четыре. или. Плюс семь, восемьсот двенадцать, четырёхсот восемьдесят, девяносто, два нуля.
    Выберите вопрос чтобы получить ответ:  
    Что такое Студенческий офис?
    Зачем мне обращаться в Студенческий офис?
    Как подать заявку на получение справки/документа о предыдущем образовании?
    Как попасть на консультацию в Студенческий офис?
    Я не знаю, кому задать вопрос. Студенческий офис поможет?
    """

buttons = [
    {
        'title': 'VK',
        'url': 'https://vk.com/student_services_office',
        'hide': False
    },
    {
        'title': 'Telegram',
        'url': 'https://t.me/itmolnia',
        'hide': False
    },
    "Что такое Студенческий офис?",
    "Зачем мне обращаться в Студенческий офис?",
    "Как подать заявку на получение справки/документа о предыдущем образовании?",
    "Как попасть на консультацию в Студенческий офис?",
    "Я не знаю, кому задать вопрос. Студенческий офис поможет?",
    'Что ты умеешь?',
    "Помощь",
    "Назад",
    "Выйти"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'СТУДЕНЧЕСКИЙ ОФИС',
    'description': \
        """
        Почта: so@itmo.ru.. Телефон: +7 (812) 607-04-74 или +7 (812) 480-90-00..
        Выберите вопрос чтобы получить ответ:
        Что такое Студенческий офис?
        Зачем мне обращаться в Студенческий офис?
        Как подать заявку на получение справки/документа о предыдущем образовании?
        Как попасть на консультацию в Студенческий офис?
        Я не знаю, кому задать вопрос. Студенческий офис поможет?
        """
}

session_state = {
    "branch": "studentOffice"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
