import copy

globalStorage = {}

def addInGlobalStorage(key, data, overwrite=False):
    if key in globalStorage and not overwrite:
        raise ValueError('Global storage already have field with key ' + key + '.\nUse overwrite=True to allow overwrite')
    newData = copy.deepcopy(data)
    globalStorage[key] = newData

def removeFromGlobalStorage(key):
    del globalStorage[key]