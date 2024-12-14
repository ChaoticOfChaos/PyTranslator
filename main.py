import morse
import binary
import hex
import hash

text = "Hello There, Friend"

# Morse
morseText = morse.translateToMorse(text)
print(morseText)
plainText = morse.translateMorseToText(morseText)
print(plainText)


# Binário
binaryText = binary.translateToBinary(text)
print(binaryText)
plainText2 = binary.translateBinaryToText(binaryText)
print(plainText2)


# Hexa
# -> Hexa (root)
textRoot = "0 1 2 3 4 5 6 7 8 9 a b c d e f"
HexRootText = hex.translateToHex(textRoot)
print(HexRootText)
plainText3 = hex.translateHexToText(HexRootText)
print(plainText3)

# -> Hex (alpha)
HexAlphaText = hex.translateToHexAlpha(text)
print(HexAlphaText)
plainText4 = hex.translateHexAlphaToText(HexAlphaText)
print(plainText4)


# Hash
Hash = hash.HashFy(text)
print(Hash.MD5())
print(Hash.Sha1())
print(Hash.Sha224())
print(Hash.Sha256())
print(Hash.Sha3_224())
print(Hash.Sha3_256())
print(Hash.Sha3_384())
print(Hash.Sha3_512())
print(Hash.Sha384())
print(Hash.Sha512())