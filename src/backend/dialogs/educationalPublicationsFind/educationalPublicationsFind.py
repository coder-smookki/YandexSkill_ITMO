from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, context):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event, context):
    return isInContext(event, 'educationalPublications')


educationalPublicationsFind = {'getResponse': getResponse, 'isTriggered': isTriggered}