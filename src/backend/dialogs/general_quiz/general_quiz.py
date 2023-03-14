from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"викторина", "виктори", "start_quiz", "квиз"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


library = {'getResponse': getResponse, 'isTriggered': isTriggered}
