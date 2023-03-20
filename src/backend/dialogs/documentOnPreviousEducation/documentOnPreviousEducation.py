from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"как", "подать", "заявку", "на", "получение", "справки", "документа", "о", "предыдущем", "образовании", "previous", "education", "document"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


documentOnPreviousEducation = {'getResponse': getResponse, 'isTriggered': isTriggered}
