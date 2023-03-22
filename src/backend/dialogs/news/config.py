from utils.responseHelper import getLanguage

words = {
    "ru-RU": {
        "tts":
            """
            Выберите раздел новостей, который хотите посмотреть.
            Анонсы или Контесты.
            """,
        "buttons": ["Анонсы", "Контесты", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "213044/70ec763b4e6221c9bf9a",
            "title": "НОВОСТИ",
            "description":
                """
                Выберите раздел новостей: Анонсы или Контесты.
                """,
        },
    },
    "en-US": {
        "tts":
            """
            Select the news section you want to watch.
            Announcements or Contests.
            """,
        "buttons": [
            "Announcements",
            "Contests",
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "213044/70ec763b4e6221c9bf9a",
            "title": "NEWS",
            "description":
                """
                Select the news section: Announcements or Contests.
                """,
        },
    },
}

session_state = {"branch": "news"}

def getConfig(event):
    lang = getLanguage(event)
    return {
        "tts": words[lang]["tts"],
        "buttons": words[lang]["buttons"],
        "card": words[lang]["card"],
        "session_state": session_state,
    }
