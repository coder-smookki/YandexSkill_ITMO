from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"знаю", 'кому', 'задать', 'вопрос', 'поможет', "know", 'to whom', 'ask', 'question'}
    return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


officeOtherFeatures = {'getResponse': getResponse, 'isTriggered': isTriggered}
