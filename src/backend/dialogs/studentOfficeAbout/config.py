from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts": """
                Студенческий офис – это компас студента в мире сложных и непонятных вопросов. 
    Менеджеры офиса вряд ли помогут решить задачу по математике, но точно подскажут, как заселиться в общежитие или получить социальную стипендию.
            """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/65fa68f782fa6af3f071",
            "title": "ЧТО ТАКОЕ СТУДЕНЧЕСКИЙ ОФИС?",
            "description": """
                Студенческий офис – это компас студента в мире сложных и непонятных вопросов.
                """,
        },
    },
    "en-US": {
        "tts": """
            The student office is the student's compass in the world of complex and incomprehensible issues.
    Office managers are unlikely to help solve a math problem, but they will definitely tell you how to move into a hostel or get a social scholarship.""",
        "buttons": [
            "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/65fa68f782fa6af3f071",
            "title": "WHAT IS THE STUDENT OFFICE?",
            "description": """The student office is the student's compass in the world of complex and incomprehensible issues.""",
        },
    },
}

session_state = {"branch": "studentOfficeAbout"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
