from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Библиотека ИТМО — это научно-образовательный центр, предоставляющий все возможности для вашего профессионального роста и развития:
            знакомьтесь с лучшими коллекциями ведущих отечественных и зарубежных издательств по всем отраслям научного знания,
            бронируйте необходимую литературу через личный кабинет,
            работайте в современных пространствах, организовывайте мероприятия и важные переговоры.
            Зарегистрируйте кампусную карту у библиотекаря или администратора коворкинга в качестве читательского билета и пользуйтесь всеми возможностями!
            """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "1540737/1c8b2e480345c6cc8635",
            "title": "БИБЛИОТЕКА",
            "description":
                """
                Зарегистрируйте кампусную карту у библиотекаря или администратора коворкинга в качестве читательского билета и пользуйтесь всеми возможностями!
                """,
        },
    },
    "en-US": {
        "tts":
            """
            The ITMO Library is a scientific and educational center that provides all the opportunities for your professional growth and development:
            get acquainted with the best collections of leading domestic and foreign publishing houses in all branches of scientific knowledge,
            book the necessary literature through your personal account,
            work in modern spaces, organize events and important negotiations.
            Register a campus card with a librarian or coworking administrator as a library card and enjoy all the opportunities!
            """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1540737/1c8b2e480345c6cc8635",
            "title": "LIBRARY",
            "description":
                """
Register a campus card with a librarian or coworking administrator as a library card and enjoy all the opportunities!
                """,
        },
    },
}

session_state = {"branch": "library"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
