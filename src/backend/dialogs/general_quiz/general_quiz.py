from .config import getConfig, check_answerm, getFinishConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, context):
    check_answer(event)
    if getState(event, "count_questions") < 10:
        config = getConfig(getState(event, getState(event, "count_questions")), event)
    else:
        config = getFinishConfig(event)
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"назад", "выход"}
    return not isSimilarTokens(event, token) and isInContext(event, 'start_quiz')


general_quiz = {'getResponse': getResponse, 'isTriggered': isTriggered}
