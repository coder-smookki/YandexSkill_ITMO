from .config import getConfig
from ..chessGame.config import get_config_choose_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    if isInContext(event, 'chessMain') and isSimilarTokens(event, {'правила'}):
        config = getRulesConfig()
    elif isInContext(event, 'chessMain') and isSimilarTokens(event, {'играть', 'да'}):
        config = get_config_choose_color()
    else:
        config = getConfig()
    return createResponse(event, config)

def isTriggered(event):
    token = {"шахматы", "шахмат"}
    return isSimilarTokens(event, token)


chessMain = {'getResponse': getResponse, 'isTriggered': isTriggered}
