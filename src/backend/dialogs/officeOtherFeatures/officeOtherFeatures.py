from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"знаю", 'кому', 'задать', 'вопрос', 'поможет'}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


officeOtherFeatures = {'getResponse': getResponse, 'isTriggered': isTriggered}
