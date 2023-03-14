from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"зачем", "мне", "обращаться", "в"}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


studentOfficeWhy = {'getResponse': getResponse, 'isTriggered': isTriggered}
