#https://docs.python.org/3/library/hashlib.html
import hashlib
from hmac import digest_size
from timeit import default_timer as timer

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def blake2b(self,filepath="test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = hashlib.blake2b(digest_size=64) # 8 to 512 bits

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()

        return (end-start)
    
    def blake2s(self,filepath="test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = hashlib.blake2s(digest_size=32)

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()
        
        return (end-start)

    def hashTest(self,arg,filepath="test.txt"):
        temp=0
        switch={
            "blake2b": self.blake2b,
            "blake2s": self.blake2s,
        }
        for i in range(20):
            temp+=switch[arg](filepath)
        print(temp/20)
    
    def getDigest(self):
        return self.digest

    def getHexDigest(self):
        return self.digest.hex()




# RYCHLOSTNY TEST #
myHash = Hash()
cas = myHash.blake2b() # parameter berie na vstup subor v mode rb
print("hash blake2b:",cas,"sec")

myHash = Hash()
cas = myHash.blake2s() # parameter berie na vstup subor v mode rb
print("hash blake2s:",cas,"sec")


