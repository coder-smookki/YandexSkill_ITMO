from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    config = getConfig()
    return createResponse(event, config)

def isTriggered(event):
    token = {"шахматы", "шахмат"}
    return isSimilarTokens(event, token)


chessMain = {'getResponse': getResponse, 'isTriggered': isTriggered}
