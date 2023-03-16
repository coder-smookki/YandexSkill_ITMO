from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    return isSimilarCommand(event, 'как узнать актуальность навыка на данный момент')


howToCheckRelevance = {'getResponse': getResponse, 'isTriggered': isTriggered}
