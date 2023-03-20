from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Вы перешли в категорию "Начало Викторины". 
            Вы можете начать викторину по нажатию кнопки - Начать.
            При запуске викторины, будут запущены вопросы. На которые вы должны дать правильные ответы.
            Один правильный ответ, равняется одному баллу.
            Вы готовы к викторине?    
            """,
        "buttons": [
            "Начать",
            "Повторить ещё раз",
            'Что ты умеешь?',
            "Помощь",
            "Назад",
            "Выйти"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '937455/40f0536e426907808499',
            'title': 'НАЧАЛО ВИКТОРИНЫ',
            'description':
                """
                Вы готовы начать викторину?
                """
        }
    },

    "en-US": {
        "tts":
            """
            You have moved to the "Start Quiz" category.
            You can start the quiz by pressing the Start button.
            When you start a quiz, questions will be launched. To which you must give the correct answers.
            One correct answer equals one point.
            Are you ready for the quiz?
            """,
        "buttons": [
            "Begin",
            "Repeat",
            'What can you do?',
            "Help",
            "Back",
            "Exit"
        ],

        "card": {
            'type': 'BigImage',
             'image_id': '937455/40f0536e426907808499',
             'title': 'START QUIZ',
             'description':
                 """
                 Are you ready to start the quiz?
                 """
        }
    }
}

session_state = {
    "branch": "start_quiz",
    "count_questions": 0,
    "count_correct_response": 0,
    "questions_list": []
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
