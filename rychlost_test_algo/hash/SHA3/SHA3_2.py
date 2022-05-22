# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/
from cryptography.hazmat.primitives import hashes
from timeit import default_timer as timer

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def sha3_224(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        
        hasher = hashes.Hash(hashes.SHA3_224())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()

        return (end-start)
    
    def sha3_256(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        hasher = hashes.Hash(hashes.SHA3_256())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)

    def sha3_384(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
       
        hasher = hashes.Hash(hashes.SHA3_384())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)

    def sha3_512(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        hasher = hashes.Hash(hashes.SHA3_512())

        start = timer()
        hasher.update(data)
        self.digest = hasher.finalize()
        end = timer()
        
        return (end-start)


    def hashTest(self,arg,filepath="text.txt"):
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


# RYCHLOSTNY TEST #

print("\nModul: cryptography \nAlgoritmus: SHA3-224")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_224("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: cryptography \nAlgoritmus: SHA3-256")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_256("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: cryptography \nAlgoritmus: SHA3-384")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_384("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: cryptography \nAlgoritmus: SHA3-512")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_512("test.txt"),"sec")# hasuje subor text.txt