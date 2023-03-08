def createResponse(event, config):
    return {
        'response': {
            'text': config['message'],
            'tts': config['tts'],
            'card': config['card'],
            'buttons': createButtons(config['buttons']),
            'end_session': config['end_session'] if 'end_session' in config else False
        },
        'session': event['session'],
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
