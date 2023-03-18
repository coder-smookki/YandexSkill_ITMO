from .config import getConfig, getHelpConfig
from ..chessGame.config import get_config_choose_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    if isInContext(event, 'chessMain') and isSimilarTokens(event, {'правила'}):
        config = getHelpConfig()
    elif isInContext(event, 'chessMain') and isSimilarTokens(event, {'играть', 'да'}):
        config = get_config_choose_color()
    else:
        print('123', event)
        config = getConfig()
    return createResponse(event, config)

def isTriggered(event):
    token = {"шахматы", "шахмат"}
    return isSimilarTokens(event, token) or isInContext(event, 'chessMain')


chessMain = {'getResponse': getResponse, 'isTriggered': isTriggered}
