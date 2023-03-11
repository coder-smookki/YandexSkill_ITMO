from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"зачем", "мне", "обращаться", "в"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


studentOfficeWhy = {'getResponse': getResponse, 'isTriggered': isTriggered}
