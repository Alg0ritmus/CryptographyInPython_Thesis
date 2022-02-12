from cryptography.hazmat.primitives import hashes
from timeit import default_timer as timer

# https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def sha3_224(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        
        hasher = hashes.Hash(hashes.SHA3_224())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()

        return (end-start)
    
    def sha3_256(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        hasher = hashes.Hash(hashes.SHA3_256())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)

    def sha3_384(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
       
        hasher = hashes.Hash(hashes.SHA3_384())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)

    def sha3_512(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        hasher = hashes.Hash(hashes.SHA3_512())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)


    def hashTest(self,arg,filepath="../../test.txt"):
        temp=0
        switch={
            "224": self.sha3_224,
            "256": self.sha3_256,
            "384": self.sha3_384,
            "512": self.sha3_512
        }
        for i in range(20):
            temp+=switch[arg](filepath)
        print(temp/20)
    
    def getDigest(self):
        return self.digest

    def getHexDigest(self):
        return self.digest.hex()


data="text.txt"

myHash = Hash()
myHash.hashTest("224")

myHash = Hash()
myHash.hashTest("256")

myHash = Hash()
myHash.hashTest("384")

myHash = Hash()
myHash.hashTest("512")