from .event_handler import event_handler
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = event_handler(event)
    return createResponse(event, config)


def isTriggered(event, context):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}
