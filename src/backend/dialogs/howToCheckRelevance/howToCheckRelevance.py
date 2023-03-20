from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isSimilarCommand(event, 'как узнать актуальность навыка на данный момент') or isSimilarCommand(event, 'how to find out the relevance of a skill at the moment')


howToCheckRelevance = {'getResponse': getResponse, 'isTriggered': isTriggered}
