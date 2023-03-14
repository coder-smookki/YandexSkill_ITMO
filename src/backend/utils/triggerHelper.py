def isNewSession(event):
    return event['session']['new'] is True

def isSimilarTokens(event, tokens):
    return len(list(set(event['request']['nlu']['tokens']) & tokens)) != 0

def isInContext(event, context):
    if not 'branch' in event['state']['session']:
        return False

    if isinstance(context, list):
        for elem in context:
            if elem in event['state']['session']["branch"]:
                return True
        return False
    return context in event['state']['session']["branch"]

def isSimilarCommand(event, command):
    return event['request']['command'] == command

def haveState(event, state):
    return state in event['state']['session']
