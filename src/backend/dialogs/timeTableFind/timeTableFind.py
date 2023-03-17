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
    nextPageTokens = {"дальше", "далее", "следующая", "некст", "следующий"}
    pastPageTokens = {"предыдущая", "обратно"}
    return isInContext(event, "timeTable") and (isSimilarTokens(event, nextPageTokens) or isSimilarTokens(event, pastPageTokens))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
