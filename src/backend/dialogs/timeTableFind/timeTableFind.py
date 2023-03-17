from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    countOnOnePage = 1
    if isSimilarCommand(event, 'Следующая страница'):
        lastElem = getState(event, 'lastElem')
        config = getPageConfig(event, lastElem + countOnOnePage, countOnOnePage)
    elif isSimilarCommand(event, 'Предыдущая страница'):
        lastElem = getState(event, 'lastElem')
        config = getPageConfig(event, lastElem - countOnOnePage, countOnOnePage)
    else:
        config = getConfig(event, countOnOnePage)
    print(config)
    return createResponse(event, config)
    
def isTriggered(event):
    nextPageTokens = {"дальше", "далее", "следующая", "некст", "следующий"}
    pastPageTokens = {"предыдущая", "обратно"}
    return isInContext(event, "timeTable") and (isSimilarTokens(event, nextPageTokens) or isSimilarTokens(event, pastPageTokens))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
