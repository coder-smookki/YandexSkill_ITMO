from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd
import copy

config = getConfig()


def getResponse(event, allDialogs=None):
    if isInContext(event, 'exitConfirm') and isSimilarCommand(event, 'да'):
        newConfig = {'response': {
            'text': config['message'],
            'tts': config['tts'],
            'card': config['card'] if 'card' in config else {},
            'buttons': createButtons(config['buttons']),
            'end_session': config['end_session'] if 'end_session' in config else False
        },
            'session': event['session'],
            'session_state': config['session_state'] if 'session_state' in config else {'branch': ''},
            'version': event['version']}
        newConfig['end_session'] = True
        return createResponse(event, newConfig)
    elif isInContext(event, 'exitConfirm'):
        return getDialogResponseFromEnd(event, 2, allDialogs)
    return createResponse(event, config)


def isTriggered(event):
    return isSimilarCommand(event, 'выйти') or isInContext(event, 'exitConfirm') and isSimilarCommand(event, 'да')


exitConfirm = {'getResponse': getResponse, 'isTriggered': isTriggered}
