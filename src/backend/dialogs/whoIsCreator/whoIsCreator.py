from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isSimilarCommand(event, 'кто создатели навыка') or isSimilarCommand(event,
                                                                               'who are the creators of the skill')


whoIsCreator = {'getResponse': getResponse, 'isTriggered': isTriggered}
