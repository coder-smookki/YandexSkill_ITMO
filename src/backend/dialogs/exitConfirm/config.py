from utils.responseHelper import getLanguage

config = {
    "ru-RU": {
        "tts": """
            Вы уверены в том, что хотите выйти?
            """,
        "buttons": [
            "Да",
            "Нет",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "ВЫЙТИ ИЗ НАВЫКА?",
            "description": """
                Вы уверены в том, что хотите выйти?
                """,
        },
    },
    "en-US": {
        "tts": """
            Are you sure you want to exit?
            """,
        "buttons": [
            "Yes",
            "No",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "EXIT SKILL?",
            "description": """
                Are you sure you want to exit?
                """,
        },
    },
}

session_state = {"branch": "exitConfirm"}


def getConfig(event):
    lang = getLanguage(event)
    
    return {
        "tts": config[lang]['tts'],
        "buttons": config[lang]['buttons'],
        "card": config[lang]['card'],
        "session_state": config[lang]['session_state'],
    }
