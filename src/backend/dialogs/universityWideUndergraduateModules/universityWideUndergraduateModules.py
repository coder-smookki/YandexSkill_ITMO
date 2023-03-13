from . import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"общеуниверситетские", "модули", "в", "бакалавриате"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


universityWideUndergraduateModules = {'getResponse': getResponse, 'isTriggered': isTriggered}
