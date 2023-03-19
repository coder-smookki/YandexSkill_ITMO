from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import *
import copy

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"учебные", "издания", "учебны"}
    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu')


educationalPublications = {'getResponse': getResponse, 'isTriggered': isTriggered}
