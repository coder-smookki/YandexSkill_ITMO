from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isSimilarCommand(event, 'как связаться с разработчиками') or isSimilarCommand(event,
                                                                                         'how to contact developers')


howToConnectWithDevelopers = {'getResponse': getResponse, 'isTriggered': isTriggered}
