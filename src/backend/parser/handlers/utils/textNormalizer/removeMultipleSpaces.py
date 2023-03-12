import re

def removeMultipleSpaces(string):
    return re.sub(r'\s+', ' ', string)