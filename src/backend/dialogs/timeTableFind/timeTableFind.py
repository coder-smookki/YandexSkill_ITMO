from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    if isSimilarCommand(event, 'Следующая страница'):
        pass
    if isSimilarCommand(event, 'Предыдущая страница'):
        pass

    config = getConfig(event)
    return createResponse(event, config)
    
def isTriggered(event):
    return False


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
