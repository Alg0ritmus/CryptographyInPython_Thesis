# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://www.pycryptodome.org/en/latest/src/cipher/chacha20.html
from Cryptodome.Cipher import ChaCha20
import base64
import os
from timeit import default_timer as timer


class chacha20:
    def __init__(self) -> None:
        self.key = os.urandom(32)
        self.nonce = os.urandom(12) #12-Byte random nonce
        self.ct = None
        self.pt = None

    def encrypt(self,filepath="../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        

        chacha = ChaCha20.ChaCha20Cipher(self.key,self.nonce)

        start = timer()
        self.ct = chacha.encrypt(data)
        end = timer()
        return (end - start)

    def decrypt(self):
        chacha = ChaCha20.ChaCha20Cipher(self.key,self.nonce)
        start = timer()
        self.pt = chacha.decrypt(self.ct)
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
myChaCHa = chacha20()

print("\nModul: PyCryptodome \nAlgoritmus: ChaCha20\n" + "spracovanie 100MB suboru:",myChaCHa.encrypt(filepath_),"sec")
#print(myChaCHa.getCT())
#
#myChaCHa.decrypt()
#print(myChaCHa.getPT())