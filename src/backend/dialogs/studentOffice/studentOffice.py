from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"студенческий", "студенчески", "студенческ", "офис", "офисс", "офи"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


studentOffice = {'getResponse': getResponse, 'isTriggered': isTriggered}
