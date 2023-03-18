from .event_move import event_move
from .event_color import event_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    def getReponseFunc(event, allDialogs):
        try:
            getState(event, 'orientation')
        except KeyError as e:
            raise KeyError('Orientation = 0 KAK SUDA POPALO?')
            # raise e
        a = createResponse(event, event_move(event))
        print(a)
        return a

    try:
        orientation = getState(event, 'orientation')
    except KeyError:
        orientation = None
    if orientation:  # т.е. играет и есть цвет
        return createTimeoutResponse(event, allDialogs, getReponseFunc, 'chessGameTimeout')
    else:
        return createResponse(event, event_color(event))


def isTriggered(event):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}