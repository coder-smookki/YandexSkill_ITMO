from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Вы направились в категорию "Связь с разработчиками".
    Все контакты описаны в письменной части навыка, к сожалению голосом не получится озвучить контакты. Так как происходят проблемы с произношением.
            """,
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выйти"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '937455/40f0536e426907808499',
            'title': 'СВЯЗЬ С РАЗРАБОТЧИКАМИ',
            'description':
                """
                Ильин Кирилл (Тим Лидер): tg - https://t.me/ShVePs86, email - medved3loy@yandex.ru, discord - Shveps#9488...
                Плюснин Александр (Главный Разработчик): tg - https://t.me/elogrus, email - null, discord - elogrus#7802...
                Караваев Иван (Разработчик): tg - https://t.me/Nauryeasy, email - null, discord - 1_-NauRy-_1#2298...
                Лесовой Кирилл (Тестировщик): tg - https://t.me/K1rLes, email - null, discord - K1rLes#3663...
                Кутников Родион (Дизайнер): tg - https://t.me/Zl0yKobra, email - null, discord - IT_Технократ#7295...
                """
        }
    },

    "en-US": {
        "tts":
            """
            You are directed to the category "Contact Developers".
    All contacts are described in the written part of the skill, unfortunately it will not be possible to voice contacts. Because there are problems with pronunciation.
            """,
        "buttons": [
            "Repeat one more time"
            "What can you do?",
            "Back",
            "Exit"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '937455/40f0536e426907808499',
            'title': 'CONTACT DEVELOPERS',
            'description':
                """
                Kirill Ilyin (Tim Leader): tg - https://t.me/ShVePs86, email - medved3loy@yandex.ru, discord - Shveps#9488...
                Plyusnin Alexander (Chief Developer): tg - https://t.me/elogrus, email - null, discord - elogrus#7802...
                Karavaev Ivan (Developer): tg - https://t.me/Nauryeasy, email - null, discord - 1_-NauRy-_1#2298...
                Kirill Lesovoy (Tester): tg - https://t.me/K1rLes, email - null, discord - K1rLes#3663...
                Kutnikov Rodion (Designer): tg - https://t.me/Zl0yKobra, email - null, discord - IT_Technocrat #7295...
                """
        }
    }
}

session_state = {
    "branch": "howToConnectWithDevelopers"
}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
