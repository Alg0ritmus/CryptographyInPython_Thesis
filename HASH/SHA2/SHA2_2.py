from cryptography.hazmat.primitives import hashes
from timeit import default_timer as timer

# https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def sha2_224(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        

        hasher = hashes.Hash(hashes.SHA224())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()

        return (end-start)
    
    def sha2_256(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        hasher = hashes.Hash(hashes.SHA256())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)

    def sha2_384(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        hasher = hashes.Hash(hashes.SHA384())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)

    def sha2_512(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
 
        hasher = hashes.Hash(hashes.SHA512())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)


    def hashTest(self,arg,filepath="../../test.txt"):
        temp=0
        switch={
            "224": self.sha2_224,
            "256": self.sha2_256,
            "384": self.sha2_384,
            "512": self.sha2_512
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