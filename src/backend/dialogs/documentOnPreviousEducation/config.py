from utils.responseHelper import getLanguage

config = {
    "ru-RU": {
        "tts": """
            Чтобы подать заявку на получение документа о предыдущем образование, вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
            """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/65fa68f782fa6af3f071",
            "title": "ДОКУМЕНТ О ПРЕДЫДУЩЕМ ОБРАЗОВАНИИ",
            "description": """
                Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
                """,
        },
    },
    "en-US": {
        "tts":
            """
            You need to go to the ISU portal, and then everything is simple! Submit an application through the form offered by the system.
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
            "image_id": "1521359/65fa68f782fa6af3f071",
            "title": "PREVIOUS EDUCATION DOCUMENT",
            "description":
                """
                You need to go to the ISU portal, and then everything is simple! Submit an application through the form offered by the system.
                """,
        },
    },
}

session_state = {"branch": "documentOnPreviousEducation"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
