from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    def getReponseFunc(event, allDialogs):
        config = copy.deepcopy(getConfig(event))
        print(config)
        return createResponse(event,config)
    return createTimeoutResponse(event, allDialogs, getReponseFunc, 'educationPublication')

def isTriggered(event):
    return isInContext(event, 'educationalPublications')


educationalPublicationsFind = {'getResponse': getResponse, 'isTriggered': isTriggered}