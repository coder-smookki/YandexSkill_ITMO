from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"как", "подать", "заявку", "на", "получение", "справки", "документа", "о", "предыдущем", "образовании"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


documentOnPreviousEducation = {'getResponse': getResponse, 'isTriggered': isTriggered}
