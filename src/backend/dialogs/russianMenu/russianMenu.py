from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    config = getConfig(event)
    a = createResponse(event, config)
    # print(a)
    return a


def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


russianMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
