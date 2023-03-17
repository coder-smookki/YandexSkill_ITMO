from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    countOnOnePage = 3
    if isSimilarCommand(event, 'Следующая страница'):
        lastElem = getState(event, 'lastElem')
        config = getConfig(event, lastElem + countOnOnePage, countOnOnePage)
    elif isSimilarCommand(event, 'Предыдущая страница'):
        lastElem = getState(event, 'lastElem')
        config = getConfig(event, lastElem - countOnOnePage, countOnOnePage)
    else:
        config = getConfig(event)
    print(config)
    return createResponse(event, config)
    
def isTriggered(event):
    nextPageTokens = {"дальше", "далее", "следующая", "некст", "следующий"}
    pastPageTokens = {"предыдущая", "обратно"}
    return isInContext(event, "timeTable") and (isSimilarTokens(event, nextPageTokens) or isSimilarTokens(event, pastPageTokens))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
