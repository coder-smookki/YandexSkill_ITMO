from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    def getResponseFunc():
        config = getConfig(event)
        createResponse(event, config)
    return createTimeoutResponse(event, allDialogs, getResponseFunc, 'timeTable')
    
def isTriggered(event):
    return isInContext(event, 'timeTable') and isSimilarTokens(event, {'еще', 'ещё', 'попробовать', 'заново'})


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
