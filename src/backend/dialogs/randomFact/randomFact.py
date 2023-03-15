from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event):
    token = {"еще", "факты", "факт"}
    return isSimilarTokens(event, token) and (isInContext(event, 'russianMenu') or isInContext(event, 'randomFact'))


randomFact = {'getResponse': getResponse, 'isTriggered': isTriggered}