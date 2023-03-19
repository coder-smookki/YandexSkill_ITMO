import json
import copy
import random
from utils.responseHelper import *

with open("questions.json") as file:
    questions = json.loads(file.read())

buttons = [
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"
]

session_state = {
    "branch": "start_quiz"
}


def getConfig(event):
    message = questions["questions"][getState(event, "questions_list")[-1]]
    correct_answer = questions["answers"][getState(event, "questions_list")[-1]]
    answers = copy.deepcopy(questions["uncorrect_answers"])
    answers[random.randint(0, len(answers) - 1)] = correct_answer
    buttons_response = answers + buttons
    states = {
        "count_questions": event["state"]["session"]["count_questions"],
        "count_correct_response": event["state"]["session"]["count_correct_response"],
        "questions_list": event['state']['session']['questions_list']
    }

    states.update(session_state)

    return {
        'message': message,
        'tts': message,
        'buttons': buttons_response,
        'session_state': states
    }


def getFinishConfig(event):
    return {
        'message': "Ваш результат: " + str(getState(event, "count_correct_response") + 1) + "/" + str(getState(event, "count_questions")),
        'tts': "Ваш результат:" + str(getState(event, "count_correct_response") + 1) + "из" + str(getState(event, "count_questions")),
        'buttons': buttons,
        'session_state': {
            "branch": "russianMenu"
        }
    }


def check_answer(event):
    try:
        if questions["answers"][getState(event, "questions_list")[-1]] == getOriginalUtterance(event):
            setStateInEvent(event, "count_correct_response", getState(event, "count_correct_response") + 1)
    except:
        pass
    setStateInEvent(event, "count_questions", getState(event, "count_questions") + 1)

    questions_list = getState(event, "questions_list")
    track_question = random.randint(0, len(questions['questions'] - 1))
    while track_question in questions_list:
        track_question = random.randint(0, len(questions['questions'] - 1))

    questions_list.append(track_question)

    setStateInEvent(event, "questions_list", questions_list)