from .event_move import event_move
from .event_color import event_color
from utils.dialogCreator import *
from utils.triggerHelper import *


def getResponse(event, context):
    if event["state"]["session"].get("orientation"):
        config = event_move(event)
    else:
        config = event_color(event)

    return createResponse(event, config)


def isTriggered(event, context):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}
