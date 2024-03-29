def isNewSession(event):
    return event['session']['new'] is True


def isSimilarTokens(event, tokens):
    return len(list(set(event['request']['nlu']['tokens']) & tokens)) != 0

def isInCommandOr(event, arr):
    command = event["request"]['command']
    for elem in arr:
        if elem in command:
            return True
    return False

def isInCommandAnd(event, arr):
    command = event["request"]['command']
    for elem in arr:
        if not (elem in command):
            return False
    return True

def isInContext(event, context):
    if not 'branch' in event['state']['session']:
        return False

    if isinstance(context, list):
        for elem in context:
            if elem in event['state']['session']["branch"]:
                return True
        return False
    return context in event['state']['session']["branch"]


def isInLastContext(event, context):
    if not 'branch' in event['state']['session']:
        return False

    if isinstance(context, list):
        for elem in context:
            if elem == event['state']['session']["branch"][-1]:
                return True
        return False
    return context == event['state']['session']["branch"][-1]


def isSimilarCommand(event, command):
    return event['request']['command'] == command


def haveState(event, state):
    return state in event['state']['session']


def haveGlobalState(event, state):
    return 'user' in event['state'] and state in event['state']['user']
