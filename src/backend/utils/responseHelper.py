import copy


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
