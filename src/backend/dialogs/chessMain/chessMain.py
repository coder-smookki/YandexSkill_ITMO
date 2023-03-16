from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)

def isTriggered(event, context):
    token = {"шахматы", "шахмат"}
    return isSimilarTokens(event, token)


chessMain = {'getResponse': getResponse, 'isTriggered': isTriggered}
