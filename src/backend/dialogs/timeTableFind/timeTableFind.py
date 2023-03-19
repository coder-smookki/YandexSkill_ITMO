from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *

nextPageTokens = {"дальше", "далее", "следующая", "некст", "следующий"}
pastPageTokens = {"предыдущая", "обратно"}


def getResponse(event, allDialogs=None):
    countOnOnePage = 2
    if isSimilarTokens(event, nextPageTokens):
        lastPage = getState(event, 'timeTable_lastPage')
        config = getPageConfig(event, lastPage + 1, countOnOnePage)
    elif isSimilarTokens(event, pastPageTokens):
        lastPage = getState(event, 'timeTable_lastPage')
        config = getPageConfig(event, lastPage - 1, countOnOnePage)
    else:
        config = getConfig(event, countOnOnePage)
    return createResponse(event, config)


def isTriggered(event):
    return isInContext(event, "timeTable") and (
                isSimilarTokens(event, nextPageTokens) or isSimilarTokens(event, pastPageTokens))


timeTableFind = {'getResponse': getResponse, 'isTriggered': isTriggered}
