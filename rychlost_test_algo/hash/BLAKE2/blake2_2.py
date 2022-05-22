# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/?highlight=blake2#blake2
from cryptography.hazmat.primitives import hashes
from timeit import default_timer as timer

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def blake2b(self,filepath="test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher =  hashes.Hash(hashes.BLAKE2b(64)) # 8 to 512 bits -> 64 bytes = 512 bits

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()

        return (end-start)
    
    def blake2s(self,filepath="test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = hashes.Hash(hashes.BLAKE2s(32)) # 8 to 256 bits -> 32 bytes = 256 bits

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
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
print("\nModul: cryptography \nAlgoritmus: Blake2b")
myHash = Hash()
#cas = myHash.blake2b() # parameter berie na vstup subor v mode rb
print("spracovanie 100MB suboru:",myHash.blake2b("test.txt"),"sec")

print("\nModul: cryptography \nAlgoritmus: Blake2s")
myHash = Hash()
#cas = myHash.blake2s() # parameter berie na vstup subor v mode rb
print("spracovanie 100MB suboru:",myHash.blake2s("test.txt"),"sec")