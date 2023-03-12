from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"общеуниверситетские", "модули", "в", "бакалавриате"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


universityWideUndergraduateModules = {'getResponse': getResponse, 'isTriggered': isTriggered}
