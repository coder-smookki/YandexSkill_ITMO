from .removeMultipleSpaces import removeMultipleSpaces
from .removeCharacters import removeCharacters
from .checkNullString import checkNullString
 
def textNormalizer(string):
    if checkNullString(string) == False:
        return False
    string = string.strip()
    string = removeMultipleSpaces(string)
    string = removeCharacters(string, [u'\xa0'])
    return string