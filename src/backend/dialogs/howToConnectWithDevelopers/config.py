message = \
    """
    Связь с разработчиками навыка:
    Ильин Кирилл (Тим Лидер): tg - https://t.me/ShVePs86, email - medved3loy@yandex.ru, discord - Shveps#9488.
    Плюснин Алексадр (Главный Разработчик): tg - https://t.me/elogrus, email - null, discord - elogrus#7802.
    Караваев Иван (Помощник Главного Разработчика): tg - https://t.me/Nauryeasy, email - null, discord - 1_-NauRy-_1#2298.
    Лесовой Кирилл (Тестировщик): tg - https://t.me/K1rLes, email - null, discord - K1rLes#3663.
    Кутников Родион (Дизайнер): tg - https://t.me/Zl0yKobra, email - null, discord - IT_Технократ#7295
    """

tts = \
    """ 
    Ильин Кирилл. Тим Лидер: Телеграм - @ShVePs86, Почта - medved3loy@yandex.ru, Дискорд - Shveps#9488.
    Плюснин Алексадр. Главный Разработчик: Телеграм - @elogrus, Почта - Нету, Дискорд - elogrus#7802.
    Караваев Иван. Помощник Главного Разработчика: Телеграм - @Nauryeasy, Почта - Нету, Дискорд - 1_-NauRy-_1#2298.
    Лесовой Кирилл. Тестировщик: Телеграм - @K1rLes, Почта - Нету, Дискорд - K1rLes#3663.
    Кутников Родион. Дизайнер: Телеграм - @Zl0yKobra, Почта - Нету, Дискорд - IT_Технократ#7295
    """

buttons = [
    "Повторить ещё раз",
    "Назад",
    "Выйти"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'СВЯЗЬ С РАЗРАБОТЧИКАМИ',
    'description':
    """
    Ильин Кирилл (Тим Лидер): tg - https://t.me/ShVePs86, email - medved3loy@yandex.ru, discord - Shveps#9488...
    Плюснин Алексадр (Главный Разработчик): tg - https://t.me/elogrus, email - null, discord - elogrus#7802...
    Караваев Иван (Помощник Главного Разработчика): tg - https://t.me/Nauryeasy, email - null, discord - 1_-NauRy-_1#2298...
    Лесовой Кирилл (Тестировщик): tg - https://t.me/K1rLes, email - null, discord - K1rLes#3663...
    Кутников Родион (Дизайнер): tg - https://t.me/Zl0yKobra, email - null, discord - IT_Технократ#7295...
    """
}

session_state = {
    "branch": "howToConnectWithDevelopers"
}

def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
