message = \
    """
    Вы направились в категорию "Стипендии".
    Учеба идет проще, когда тебя хвалят, именно поэтому в Университете ИТМО существуют разные стипендиальные выплаты. Они нацелены на стимулирование и поддержку студентов во время обучения.
    Существует множество видов стипендиальных выплат:
    Государственная академическая стипендия;
    Повышенная государственная академическая стипендия;
    Государственная стипендия аспирантам, ординаторам, ассистентам-стажерам;
    Государственная социальная стипендия;
    Материальная поддержка студентам и аспирантам;
    Стипендия Президента РФ и Правительства РФ;
    Конкурс стипендий Президента РФ для обучения за рубежом;
    Именная стипендия Правительства Санкт-Петербурга;
    Стипендия «Альфа-Шанс»;
    Стипендия фонда Владимира Потанина.
    Есть вопросы? Задайте их Стипендиальной комиссии!
    """

tts = \
    """
    Вы направились в категорию "Стипендии".
    Учеба идет проще, когда тебя хвалят, именно поэтому в Университете ИТМО существуют разные стипендиальные выплаты. Они нацелены на стимулирование и поддержку студентов во время обучения.
    Существует множество видов стипендиальных выплат:
    Государственная академическая стипендия;
    Повышенная государственная академическая стипендия;
    Государственная стипендия аспирантам, ординаторам, ассистентам-стажерам;
    Государственная социальная стипендия;
    Материальная поддержка студентам и аспирантам;
    Стипендия Президента РФ и Правительства РФ;
    Конкурс стипендий Президента РФ для обучения за рубежом;
    Именная стипендия Правительства Санкт-Петербурга;
    Стипендия «Альфа-Шанс»;
    Стипендия фонда Владимира Потанина.
    Есть вопросы? Задайте их Стипендиальной комиссии!
    """

buttons = [
    {
        'title': 'Сайт стипендии',
        'url': 'https://student.itmo.ru/ru/scholarship/',
        'hide': False
    },
    'Повторить ещё раз',
    'Помощь',
    'Назад',
    'Выйти'
]

card = {
    'type': 'BigImage',
    'image_id': '1533899/b86b0073c0e88e67d092',
    'title': 'СТИПЕНДИИ',
    'description':
        """
        Есть вопросы? Задайте их Стипендиальной комиссии! Почта - ursi@itmo.ru
        """
}

session_state = {
    "branch": "scholarships"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
