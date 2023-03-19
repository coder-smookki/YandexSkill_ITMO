from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    return isSimilarCommand(event, 'кто создатели навыка') or isSimilarCommand(event, 'who are the creators of the skill')


whoIsCreator = {'getResponse': getResponse, 'isTriggered': isTriggered}
