import hashlib

class HashFy:
    def __init__(self, text: str) -> None:
        self.plainText = text

    def Sha1(self) -> str:
        return hashlib.sha1(self.plainText.encode()).hexdigest()
    
    def Sha224(self) -> str:
        return hashlib.sha224(self.plainText.encode()).hexdigest()
    
    def Sha256(self) -> str:
        return hashlib.sha256(self.plainText.encode()).hexdigest()
    
    def Sha384(self) -> str:
        return hashlib.sha384(self.plainText.encode()).hexdigest()
    
    def Sha512(self) -> str:
        return hashlib.sha512(self.plainText.encode()).hexdigest()
    
    def MD5(self) -> str:
        return hashlib.md5(self.plainText.encode()).hexdigest()
    
    def Sha3_224(self) -> str:
        return hashlib.sha3_224(self.plainText.encode()).hexdigest()
    
    def Sha3_256(self) -> str:
        return hashlib.sha3_256(self.plainText.encode()).hexdigest()
    
    def Sha3_384(self) -> str:
        return hashlib.sha3_384(self.plainText.encode()).hexdigest()
    
    def Sha3_512(self) -> str:
        return hashlib.sha3_512(self.plainText.encode()).hexdigest()
    
