from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
            Вы можете начать викторину сказав фразу "Начать" или нажав на кнопку.
            Так же вы можете выйди с викторины, сказав фразу "Назад" или нажав на кнопку.
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
            'image_id': '1521359/ffc9c8afbe8b9f6f95c9',
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
            You can start the quiz by saying the phrase "Start" or by clicking on the button.
            You can also exit the quiz by saying the phrase "Back" or by clicking on the button.
            When you start the quiz, questions will be started. To which you must give the correct answers.
            One correct answer equals one point.
            Are you ready for the quiz?
            """,
        "buttons": [
            "Start",
            "Repeat",
            'What can you do?',
            "Help",
            "Back",
            "Exit"
        ],

        "card": {
            'type': 'BigImage',
             'image_id': '1521359/ffc9c8afbe8b9f6f95c9',
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
