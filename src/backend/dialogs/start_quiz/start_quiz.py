from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs):
    return createResponse(event, config)


def isTriggered(event):
    token = {"викторина", "виктори", "start_quiz", "квиз"}
    return isSimilarTokens(event, token) and isInContext(event, 'mainMenu')


start_quiz = {'getResponse': getResponse, 'isTriggered': isTriggered}
