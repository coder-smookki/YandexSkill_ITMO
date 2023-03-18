from .event_move import event_move, handler_not_a_move, pre_handle_move
from .event_color import event_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    def getReponseFunc(event, allDialogs):
        getState(event, 'orientation')
        move, session_states = pre_handle_move(event)
        return createResponse(event, event_move(event, move, session_states))

    if config := handler_not_a_move(event):
        return createResponse(event, config)
    try:
        getState(event, 'orientation')
        values = pre_handle_move(event)
        if isinstance(values, dict):
            return createResponse(event, values)
        return createTimeoutResponse(event, allDialogs, getReponseFunc, 'chessGameTimeout')
    except KeyError:
        return createResponse(event, event_color(event))


def isTriggered(event):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}