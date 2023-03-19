from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"зачем", "мне", "обращаться", "в", "why", "me", "contact", "in"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


studentOfficeWhy = {'getResponse': getResponse, 'isTriggered': isTriggered}
