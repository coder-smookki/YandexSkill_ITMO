from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"стипендии", "степуха", 'scholarships'}
    return isSimilarTokens(event, token) and isInContext(event, 'mainMenu')


scholarships = {'getResponse': getResponse, 'isTriggered': isTriggered}
