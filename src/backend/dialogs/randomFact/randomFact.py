from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event):
    token = {"факты", "факт"}
    tokenRepeat = {"еще"}
    return (isSimilarTokens(event, token) and isInContext(event, "russianMenu")) or (
        (isInContext(event, "randomFact") and isSimilarTokens(event, tokenRepeat))
    )


randomFact = {"getResponse": getResponse, "isTriggered": isTriggered}
