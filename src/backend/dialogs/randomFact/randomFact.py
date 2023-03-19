from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"факты", "факт", "random", "fact"}
    tokenRepeat = {"еще"}
    return (isSimilarTokens(event, token) and isInContext(event, "mainMenu")) or (
        (isInContext(event, "randomFact") and isSimilarTokens(event, tokenRepeat))
    )


randomFact = {"getResponse": getResponse, "isTriggered": isTriggered}
