from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *

nextPageTokens = {"дальше", "далее", "следующая", "некст", "следующий"}
pastPageTokens = {"предыдущая", "обратно"}

def getResponse(event, allDialogs=None):
    countOnOnePage = 1
    if isSimilarTokens(event, nextPageTokens):
        lastElem = getState(event, 'lastElem')
        config = getPageConfig(event, lastElem + countOnOnePage, countOnOnePage)
    elif isSimilarTokens(event, pastPageTokens):
        lastElem = getState(event, 'lastElem')
        config = getPageConfig(event, lastElem - countOnOnePage, countOnOnePage)
    else:
        config = getConfig(event, countOnOnePage)
    print(config)
    return createResponse(event, config)
    
def isTriggered(event):
    return isInContext(event, "timeTable") and (isSimilarTokens(event, nextPageTokens) or isSimilarTokens(event, pastPageTokens))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
