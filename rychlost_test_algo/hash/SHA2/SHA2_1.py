# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://docs.python.org/3/library/hashlib.html
import hashlib
from timeit import default_timer as timer

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def sha2_224(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = hashlib.sha224()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()

        return (end-start)
    
    def sha2_256(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = hashlib.sha256()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()
        
        return (end-start)

    def sha2_384(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = hashlib.sha384()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()
        
        return (end-start)

    def sha2_512(self,filepath="text.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        hasher = hashlib.sha512()

        start = timer()
        hasher.update(data)
        self.digest = hasher.digest()
        end = timer()
        
        return (end-start)


    def hashTest(self,arg,filepath="text.txt"):
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


# RYCHLOSTNY TEST #

print("\nModul: Hashlib \nAlgoritmus: SHA2-224")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha2_224("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: Hashlib \nAlgoritmus: SHA2-256")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha2_256("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: Hashlib \nAlgoritmus: SHA2-384")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha2_384("test.txt"),"sec")# hasuje subor text.txt

print("\nModul: Hashlib \nAlgoritmus: SHA2-512")
myHash = Hash()
print("spracovanie 100MB suboru:",myHash.sha2_512("test.txt"),"sec")# hasuje subor text.txt


