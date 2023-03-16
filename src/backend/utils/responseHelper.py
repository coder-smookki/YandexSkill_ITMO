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
    if not (timeoutName + '_' + getSessionId(event) in globalStorage):
    # if not 'timeout' in globalStorage:
        def getAsyncResponse(event, allDialogs, timeoutName):
            response = getRepsonse(event, allDialogs)
            setInGlobalStorage(timeoutName + '_' + getSessionId(event), {'response': response, 'isLoaded': True}, overwrite=True)
        
        setInGlobalStorage(timeoutName + '_' + getSessionId(event), {'response': '', 'isLoaded': False}, overwrite=True)
        
        doFuncAsAsync(getAsyncResponse, [event, allDialogs, timeoutName])
        return {
            'response': {
                'text': 'Загрузка...',
                'tts': 'азазазазаз',
                # 'card': config['card'] if 'card' in config else None,
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
    
    elif globalStorage[timeoutName + '_' + getSessionId(event)]['isLoaded'] == False:
    # elif globalStorage['timeout']['isLoaded'] == False:
        return {
            'response': {
                'text': 'Все еще загрузка...',
                'tts': 'зызызызыз',
                # 'card': config['card'] if 'card' in config else None,
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
        return globalStorage[timeoutName + '_' + getSessionId(event)]['response']

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

def createLoadingResponse(event, text):
    return {
        'response': {
            'text': text,
            'tts': '<speaker audio="alice-music-horn-1.opus">',
            'buttons': createButtons(['Назад', 'Выйти']),
            'end_session': False
        },
        'session': event['session'],
        'session_state': {'branch': ''},
        'version': event['version']
    }

def getSessionId(event):
    return event['session']['session_id']

def getUserId(event):
    return event['session']['user']['user_id']