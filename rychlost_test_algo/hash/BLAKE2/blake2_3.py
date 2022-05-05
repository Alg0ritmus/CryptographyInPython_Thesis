# https://www.pycryptodome.org/en/latest/src/hash/blake2b.html?highlight=blake2
# https://www.pycryptodome.org/en/latest/src/hash/blake2s.html?highlight=blake2
from Cryptodome.Hash import BLAKE2b, BLAKE2s
from timeit import default_timer as timer

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def blake2b(self,filepath="test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = BLAKE2b.new(digest_bits=512) # 8 to 512 bits

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()

        return (end-start)
    
    def blake2s(self,filepath="test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = BLAKE2s.new(digest_bits=256) # 8 to 256

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