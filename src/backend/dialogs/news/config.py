from utils.responseHelper import getLanguage

words = {
    "ru-RU": {
        "tts": """
        Выберите раздел новостей, который хотите посмотреть.
        Анонсы или Контесты.
        """,
        "buttons": ["Анонсы", "Контесты", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "НОВОСТИ",
            "description": """
            Выберите раздел новостей: Анонсы или Контесты.
            """,
        },
    },
    "en-US": {
        "tts": """
        Select the news section you want to watch.
        Announcements or Contests.
        """,
        "buttons": [
            "Announcements",
            "Contests",
            "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "NEWS",
            "description": """
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
