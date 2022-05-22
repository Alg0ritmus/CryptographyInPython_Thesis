# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://pypi.org/project/salsa20/
from salsa20 import XSalsa20_xor
import os
from timeit import default_timer as timer



class salsa20:
    def __init__(self) -> None:
        self.key = os.urandom(32)
        self.nonce = os.urandom(24) #24-Byte random nonce
        self.ct = None
        self.pt = None

    def encrypt(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        start = timer()
        self.ct=XSalsa20_xor(data, self.nonce, self.key)
        end = timer()
        return (end - start)

    def decrypt(self):
        
        start = timer()
        self.pt = XSalsa20_xor(self.ct, self.nonce, self.key).decode()
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
filepath_ = "text.txt" # tu je mozne zmenit PT(plain-text) subor
mySalsa = salsa20()

print("šifrovanie",mySalsa.encrypt(filepath_),"sec")
#print(mySalsa.getCT())
#
#mySalsa.decrypt()
#print(mySalsa.getPT())

