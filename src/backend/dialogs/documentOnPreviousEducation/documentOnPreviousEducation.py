from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"как", "подать", "заявку", "на", "получение", "справки", "документа", "о", "предыдущем", "образовании"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


documentOnPreviousEducation = {'getResponse': getResponse, 'isTriggered': isTriggered}
