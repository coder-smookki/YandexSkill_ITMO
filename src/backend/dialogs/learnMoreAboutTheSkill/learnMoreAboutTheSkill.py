from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    words = [
        'подробнее',
        'detailed',
        'подроб',
        'дете',
        'дета',
        'детэ',
        'дите',
        'дита',
        'дитэ'
    ]
    return isInCommandOr(event, words)


howToConnectWithDevelopers = {"getResponse": getResponse, "isTriggered": isTriggered}
