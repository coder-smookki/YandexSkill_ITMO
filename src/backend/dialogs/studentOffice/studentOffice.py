from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"студенческий", "студенчески", "студенческ", "офис", "офисс", "офи"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


studentOffice = {'getResponse': getResponse, 'isTriggered': isTriggered}
