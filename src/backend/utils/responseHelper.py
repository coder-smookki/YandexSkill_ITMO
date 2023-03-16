import copy
from utils.globalStorage import *
from utils.asyncHelper import doFuncAsAsync

def createResponse(event, originalConfig):
    config = copy.deepcopy(originalConfig)
    return {
        'response': {
            'text': config['message'],
            'tts': config['tts'],
            'card': config['card'] if 'card' in config else None,
            'buttons': createButtons(config['buttons']),
            'end_session': config['end_session'] if 'end_session' in config else False
        },
        'session': event['session'],
        'session_state': config['session_state'] if 'session_state' in config else {'branch': ''},
        'version': event['version']
    }

def createTimeoutResponse(event, allDialogs, getRepsonse, timeoutName):
    fieldName = timeoutName + '_' + getSessionId(event);
    if not (fieldName in globalStorage):
        setInGlobalStorage(fieldName, {'response': '', 'isLoaded': False}, overwrite=True)
        def getAsyncResponse(event, allDialogs, timeoutName):
            response = getRepsonse(event, allDialogs)
            setInGlobalStorage(fieldName, {'response': response, 'isLoaded': True}, overwrite=True)
        doFuncAsAsync(getAsyncResponse, [event, allDialogs, timeoutName])
        return {
            'response': {
                'text': 'Загрузка...',
                'tts': 'азазазазаз',
                'buttons': createButtons([
                    'Проверить',
                    'Назад',
                    'Выход'
                ]),
                'end_session': False
            },
            'session': event['session'],
            'session_state': {'branch': ''},
            'version': event['version']
        }
    
    elif globalStorage[fieldName]['isLoaded'] == False:
        print('loading...')
        return {
            'response': {
                'text': 'Все еще загрузка...',
                'tts': 'зызызызыз',
                'buttons': createButtons([
                    'Проверить',
                    'Назад',
                    'Выход'
                ]),
                'end_session': False
            },
            'session': event['session'],
            'session_state': {'branch': ''},
            'version': event['version']
        }

    else:
        return globalStorage[fieldName]['response']

def createButtons(buttons):
    result = []
    for button in buttons:
        if isinstance(button, str):
            result.append({
                'title': button,
                'hide': True
            })
            continue
        result.append(button)

    return result

def getSessionId(event):
    return event['session']['session_id']

def getUserId(event):
    return event['session']['user']['user_id']