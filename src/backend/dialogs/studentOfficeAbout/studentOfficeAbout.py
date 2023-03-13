from . import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"что", "такое"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


studentOfficeAbout = {'getResponse': getResponse, 'isTriggered': isTriggered}
