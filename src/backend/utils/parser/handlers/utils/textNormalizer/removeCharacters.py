def removeCharacters(string, characters):
    for sym in characters:
        string = string.replace(sym, ' ')
    return string
