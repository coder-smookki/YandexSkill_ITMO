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


def getConfig(num, event):
    message = questions["questions"][num]
    correct_answer = questions["answers"][num]
    answers = questions["uncorrect_answers"]
    answers[random.randint(0, len(answers))] = correct_answer
    buttons_response = answers + buttons
    states = {
        "count_questions": event["state"]["session"]["count_questions"],
        "count_correct_response": event["state"]["session"]["count_correct_response"]
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
        'message': "Ваш результат:" + getState(event, "count_correct_response") + "/" + getState(event, "count_correct_response"),
        'tts': "Ваш результат:" + getState(event, "count_correct_response") + "/" + getState(event, "count_correct_response"),
        'buttons': buttons,
        'session_state': "russianMenu"
    }

def check_answer(event):
    if questions["answers"][getState(event, "count_questions")] == getOriginalUtterance(event):
        setStateInEvent(event, "count_correct_response", getState(event, "count_correct_response") + 1)
    setStateInEvent(event, "count_questions", getState(event, "count_questions") + 1)