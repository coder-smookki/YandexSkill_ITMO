from .event_move import event_move
from .event_color import event_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    def getReponseFunc(event, allDialogs):
        try:
            if getState(event, 'orientation'):  # т.е. играет и есть цвет
                config = event_move(event)
            else:
                config = event_color(event)
        except KeyError:
            config = event_color(event)
        return createResponse(event, config)

    try:
        if getState(event, 'orientation'):  # т.е. играет и есть цвет
            return createTimeoutResponse(event, allDialogs, getReponseFunc, 'chessGameTimeout')
        else:
            return createResponse(event, event_color(event))
    except Exception as e:
        print(e)
        return createResponse(event, event_color(event))


def isTriggered(event):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}