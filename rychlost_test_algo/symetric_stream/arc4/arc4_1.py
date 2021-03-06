# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/arc4.html
import os
from timeit import default_timer as timer
from Cryptodome.Cipher import ARC4

class Arc4:
    def __init__(self) -> None:
        self.key=os.urandom(16)
        self.ct = None
        self.pt = None


    def encrypt(self,filepath='text.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        arc4 = ARC4.new(self.key)

        start = timer()
        self.ct = arc4.encrypt(data)
        end = timer()
        return (end - start)

    def decrypt(self):
        
        arc4 = ARC4.new(self.key) # create instance of ARC4 class

        start = timer()
        self.pt=arc4.decrypt(self.ct)
        end = timer()
        return (end - start)

    def encryptTest(self):
        temp=0
        for i in range(20):
            temp+=self.encrypt()
        print(temp/20)
    
    def getPT(self):
        return self.pt

    def getCT(self):
        return self.ct
    

# RYCHLOSTNY TEST #
filepath_ = "test.txt" # tu je mozne zmenit PT(plain-text) subor
myArc = Arc4()


print("\nModul: PyCryptodome \nAlgoritmus: ARC4\n" + "spracovanie 100MB suboru:",myArc.encrypt(filepath_),"sec")
#print(myArc.getCT())

#myArc.decrypt()
#print(myArc.getPT())


