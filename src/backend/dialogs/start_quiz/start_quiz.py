from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"викторина", "викторину", "start_quiz", "квиз", "quiz", 'куиз'}
    return isSimilarTokens(event, token) and isInContext(event, 'mainMenu')


start_quiz = {'getResponse': getResponse, 'isTriggered': isTriggered}
