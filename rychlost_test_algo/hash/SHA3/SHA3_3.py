# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://www.pycryptodome.org/en/latest/src/hash/sha3_224.html?highlight=SHA3
from Cryptodome.Hash import SHA3_224, SHA3_256, SHA3_384 , SHA3_512
from timeit import default_timer as timer


class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def sha3_224(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = SHA3_224.new()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()

        return (end-start)
    
    def sha3_256(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = SHA3_256.new()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()
        
        return (end-start)

    def sha3_384(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = SHA3_384.new()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()
        
        return (end-start)

    def sha3_512(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = SHA3_512.new()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
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

print("\nModul: PyCryptodome \nAlgoritmus: SHA3-224")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_224("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: PyCryptodome \nAlgoritmus: SHA3-256")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_256("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: PyCryptodome \nAlgoritmus: SHA3-384")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_384("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: PyCryptodome \nAlgoritmus: SHA3-512")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha3_512("test.txt"),"sec")# hasuje subor text.txt