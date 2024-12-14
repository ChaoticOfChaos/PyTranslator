import lib

morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}

def translateToMorse(text: str) -> str:
    morseText = ""
    for char in text.lower():
        if lib.isInDict(char, morse):
            morseText += morse[char] + " / "

    return morseText

def translateMorseToText(text: str) -> str:
    plainText = ""
    chars = text.split(" / ")
    chars.remove('')
    
    for char in chars:
        value = lib.getKeyByValue(char, morse)
        if len(value) != 0:
            plainText += str(value[0])

    return plainText