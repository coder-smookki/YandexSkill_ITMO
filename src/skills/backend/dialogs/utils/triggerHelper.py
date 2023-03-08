def isNewSession(event):
    return event['session']['new'] == True

def isSimilarTokens(event, tokens):
    return list(set(event['request']['nlu']['tokens']) & tokens)

def isSimilarBranch(event, branchName):
    return event['state']['session']['branch'] == branchName