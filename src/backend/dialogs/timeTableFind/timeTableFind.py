from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *

nextPageTokens = {"дальше", "далее", "следующая", "некст", "следующий"}
pastPageTokens = {"предыдущая", "обратно"}

def getResponse(event, allDialogs=None):
    countOnOnePage = 1
    if isSimilarTokens(event, nextPageTokens):
        lastElem = getState(event, 'timeTable_lastElem')
        config = getPageConfig(event, lastElem + countOnOnePage, countOnOnePage)
    elif isSimilarTokens(event, pastPageTokens):
        lastElem = getState(event, 'timeTable_lastElem')
        config = getPageConfig(event, lastElem - countOnOnePage, countOnOnePage)
        print(config)
    else:
        config = getConfig(event, countOnOnePage)
    return createResponse(event, config)
    
def isTriggered(event):
    return isInContext(event, "timeTable") and (isSimilarTokens(event, nextPageTokens) or isSimilarTokens(event, pastPageTokens))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
