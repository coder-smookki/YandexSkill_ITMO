from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    words = [
        'подробнее',
        'learn',
        'about',
        'more',
        'подроб',
        'леарн',
        'лерн',
        'лирн',
        'абаут',
        'обаут',
        'эбаут',
        'море',
        'мор'
    ]
    return isInCommandOr(event, words)


learnMoreAboutTheSkill = {"getResponse": getResponse, "isTriggered": isTriggered}
