from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    if isSimilarCommand('Следующая страница'):
        pass
    if isSimilarCommand('Предыдущая страница'):
        pass

    config = getConfig(event)
    return createResponse(event, config)
    
def isTriggered(event):
    return isInContext(event, 'timeTable') and (isSimilarCommand('Следующая страница') or isSimilarCommand('Предыдущая страница'))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
