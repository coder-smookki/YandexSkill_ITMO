from .config import getConfig, check_answer, getFinishConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    check_answer(event)
    if getState(event, "count_questions") < 6:
        config = getConfig(event)
    else:
        config = getFinishConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"назад", "выход"}
    return not isSimilarTokens(event, token) and isInContext(event, 'start_quiz')


general_quiz = {'getResponse': getResponse, 'isTriggered': isTriggered}
