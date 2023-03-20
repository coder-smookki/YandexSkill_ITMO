from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"что", "такое", "what", "is"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


studentOfficeAbout = {'getResponse': getResponse, 'isTriggered': isTriggered}
