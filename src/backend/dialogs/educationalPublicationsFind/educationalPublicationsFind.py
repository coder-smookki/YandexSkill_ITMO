from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    print('1')
    config = getConfig(event)
    print('2')
    return createResponse(event, config)


def isTriggered(event):
    return isInContext(event, 'educationalPublications')


educationalPublicationsFind = {'getResponse': getResponse, 'isTriggered': isTriggered}