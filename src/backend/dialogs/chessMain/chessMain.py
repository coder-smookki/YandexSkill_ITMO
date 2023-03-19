from .config import getConfig, getHelpConfig
from ..chessGame.config import get_config_choose_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    lang = getLanguage(event)
    if isInContext(event, 'chessMain') and isSimilarTokens(event, {'правила', 'rules'}):
        config = getHelpConfig(lang)
    elif isInContext(event, 'chessMain') and isSimilarTokens(event, {'играть', 'да', 'play', 'yes'}):
        config = get_config_choose_color(lang)
    else:
        config = getConfig(lang)
    return createResponse(event, config)


def isTriggered(event):
    token = {"шахматы", "шахмат", 'chess'}
    return isSimilarTokens(event, token) or isInContext(event, 'chessMain')


chessMain = {'getResponse': getResponse, 'isTriggered': isTriggered}
