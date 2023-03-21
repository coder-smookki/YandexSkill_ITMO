from .event_move import event_move, handler_not_a_move
from .event_color import event_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    # def getReponseFunc(event, allDialogs):
    #     getState(event, 'orientation')
    #     return createResponse(event, event_move(event))
    # print(event["state"]["session"])
    if config := handler_not_a_move(event):
        return createResponse(event, config)
    try:
        getState(event, 'orientation')
        return createResponse(event, event_move(event))
        # return createTimeoutResponse(event, allDialogs, getReponseFunc, 'chessGameTimeout')
    except KeyError as chess_error:
        print(f'{chess_error=}')
        return createResponse(event, event_color(event))


def isTriggered(event):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}
