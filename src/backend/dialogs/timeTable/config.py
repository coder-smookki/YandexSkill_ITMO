from utils.responseHelper import getLanguage

words = {
    "ru-RU": {
        "askGroupMessage":
            """
            Напишите вашу группу (например, А1234)
            """,
        "askGroupTts":
            """
            Продиктуйте вашу группу. Например. А. один, два, три, четыре. Или же. А. тысяча, двести, тридцать, четыре.
            """,
        "askDegreeMessage":
            """
            Напишите ваш вид образования (бакалавриат, магистратура, специалитет)
            """,
        "askDegreeTts":
            """
            Скажите ваш вид образования. Бакалавриат, магистратура, специалитет.
            """,
        "buttons": ["Что ты умеешь?", "Помощь", "Назад", "Выйти"],
    },
    "en-US": {
        "askGroupMessage":
            """
            Write your group (eg A1234)
            """,
        "askGroupTts":
            """
            Dictate your group. For example. A. one, two, three, four. Or. A. one thousand, two hundred, thirty, four.
            """,
        "askDegreeMessage":
            """
            Write your type of education (Bachelor's, Master's, Specialist)
            """,
        "askDegreeTts":
            """
            Tell me your type of education. Bachelor's, Master's, Specialist.
            """,
        "buttons": [
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
    },
}


session_state = {"branch": "timeTable"}


def getConfig(event, askSubject):
    lang = getLanguage(event)
    if askSubject == "group":
        return {
            "message": words[lang]["askGroupMessage"],
            "tts": words[lang]["askGroupTts"],
            "buttons": words[lang]["buttons"],
            "session_state": session_state,
        }
    elif askSubject == "degree":
        return {
            "message": words[lang]["askDegreeMessage"],
            "tts": words[lang]["askDegreeTts"],
            "buttons": words[lang]["buttons"],
            "session_state": session_state,
        }
