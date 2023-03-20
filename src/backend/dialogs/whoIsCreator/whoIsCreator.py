from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    words_ru_1 = ['кто', 'созда']
    words_ru_2 = ['кто', 'разраб']
    words_ru_3 = ['кто', 'сдела']
    words_en = ['creator', "who", "ху", "креа", "креэ"]
    return isInCommandAnd(event, words_ru_1) or isInCommandAnd(event, words_ru_2) or isInCommandAnd(event, words_ru_3) or isInCommandOr(event, words_en)


whoIsCreator = {"getResponse": getResponse, "isTriggered": isTriggered}
