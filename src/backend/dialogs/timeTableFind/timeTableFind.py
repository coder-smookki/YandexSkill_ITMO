from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    createResponse(event, config)
    
def isTriggered(event):
    return isInContext(event, 'timeTable') and isSimilarTokens(event, {'еще', 'ещё', 'попробовать', 'заново'})


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
