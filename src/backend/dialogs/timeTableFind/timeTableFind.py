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
    return isInContext(event, 'timeTable') and (isSimilarCommand(event, 'Следующая страница') or isSimilarCommand(event, 'Предыдущая страница'))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
