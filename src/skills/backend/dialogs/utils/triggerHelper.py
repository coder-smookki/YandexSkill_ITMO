
def isNewSession(event):
    return event['session']['new'] is True


def isSimilarTokens(event, tokens):
    return list(set(event['request']['nlu']['tokens']) & tokens)

def isInContext(event, context):

    if not 'dialogContext' in event:
        return False

    if isinstance(context, list):
        for elem in context:
            if event['dialogContext'] == elem:
                return True
        return False
    return event['dialogContext'] == context

