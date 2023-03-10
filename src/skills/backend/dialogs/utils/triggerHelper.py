
def isNewSession(event):
    return event['session']['new'] is True


def isSimilarTokens(event, tokens):
    return list(set(event['request']['nlu']['tokens']) & tokens)

def isInContext(event, context):

    if not 'branch' in event['state']['session']:
        return False

    if isinstance(context, list):
        for elem in context:
            if event['state']['session']["branch"] == elem:
                return True
        return False
    return event['state']['session']["branch"] == context
