from .event_move import event_move
from .event_color import event_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    o = 0
    try:
        if o := getState(event, 'orientation'):  # т.е. играет и есть цвет
            config = event_move(event)
        else:
            config = event_color(event)
        print(f'--- {o}')
    except KeyError as e:
        config = event_color(event)
        print(f'--- KE {o} {e}')

    return createResponse(event, config)


def isTriggered(event):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}