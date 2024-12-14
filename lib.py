def isInDict(key: str, dictionary: dict) -> bool:
    try:
        item = dictionary[key]
        return True
        
    except KeyError:
        return False
    
def getKeyByValue(value: str, dictionary: dict) -> list:
    return [k for k, v in dictionary.items() if v == value]