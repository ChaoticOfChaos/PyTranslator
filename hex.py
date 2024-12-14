import lib

HexRoot = {
    "0": '0x0',
    "1": '0x1',
    "2": '0x2',
    "3": '0x3',
    "4": '0x4',
    "5": '0x5',
    "6": '0x6',
    "7": '0x7',
    "8": '0x8',
    "9": '0x9',
    "a": '0xa',
    "b": '0xb',
    "c": '0xc',
    "d": '0xd',
    "e": '0xe',
    "f": '0xf',
}

HexAlpha = {
    "0": '0x00',
    "1": '0x01',
    "2": '0x02',
    "3": '0x03',
    "4": '0x04',
    "5": '0x05',
    "6": '0x06',
    "7": '0x07',
    "8": '0x08',
    "9": '0x09',
    "a": '0x0a',
    "b": '0x0b',
    "c": '0x0c',
    "d": '0x0d',
    "e": '0x0e',
    "f": '0x0f',
    "g": '0x10',
    "h": '0x11',
    "i": '0x12',
    "j": '0x13',
    "k": '0x14',
    "l": '0x15',
    "m": '0x16',
    "n": '0x17',
    "o": '0x18',
    "p": '0x19',
    "q": '0x1a',
    "r": '0x1b',
    "s": '0x1c',
    "t": '0x1d',
    "u": '0x1e',
    "v": '0x1f',
    "w": '0x20',
    "x": '0x21',
    "y": '0x22',
    "z": '0x23'
}

def translateToHex(text: str) -> str:
    HexText = ""
    
    for char in text.lower():
        if lib.isInDict(char, HexRoot):
            HexText += str(HexRoot[char]) + ' '

    return HexText

def translateHexToText(text: str) -> str:
    plainText = ""

    chars = text.split(" ")

    for char in chars:
        value = lib.getKeyByValue(char, HexRoot)
        if len(value) != 0:
            plainText += str(value[0])

    return plainText

def translateToHexAlpha(text: str) -> str:
    hexText = ""

    for char in text.lower():
        if lib.isInDict(char, HexAlpha):
            hexText += HexAlpha[char] + ' '

    return hexText

def translateHexAlphaToText(text: str) -> str:
    plainText = ""
    chars = text.split(" ")
    chars.remove('')
    
    for char in chars:
        value = lib.getKeyByValue(char, HexAlpha)
        if len(value) != 0:
            plainText += str(value[0])

    return plainText
