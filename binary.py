import lib

binary = {
    "a": "01000001",
    "b": "01000010",
    "c": "01000011",
    "d": "01000100",
    "e": "01000101",
    "f": "01000110",
    "g": "01000111",
    "h": "01001000",
    "i": "01001001",
    "j": "01001010",
    "k": "01001011",
    "l": "01001100",
    "m": "01001101",
    "n": "01001110",
    "o": "01001111",
    "p": "01010000",
    "q": "01010001",
    "r": "01010010",
    "s": "01010011",
    "t": "01010100",
    "u": "01010101",
    "v": "01010110",
    "w": "01010111",
    "x": "01011000",
    "y": "01011001",
    "z": "01011010",
    "0": "00110000",
    "1": "00110001",
    "2": "00110010",
    "3": "00110011",
    "4": "00110100",
    "5": "00110101",
    "6": "00110110",
    "7": "00110111",
    "8": "00111000",
    "9": "00111001"
}

def translateToBinary(text: str) -> str:
    binaryText = ""
    for char in text.lower():
        if lib.isInDict(char, binary):
            binaryText += str(binary[char]) + " "
    
    return binaryText

def translateBinaryToText(text: str) -> str:
    plainText = ""
    chars = text.split(" ")
    chars.remove('')
    
    for char in chars:
        value = lib.getKeyByValue(char, binary)
        if len(value) != 0:
            plainText += str(value[0])

    return plainText