# https://pycryptodome.readthedocs.io/en/latest/src/cipher/salsa20.html
from Cryptodome.Cipher import Salsa20
import os
from timeit import default_timer as timer

class salsa20:
    def __init__(self) -> None:
        self.key=os.urandom(32)
        self.nonce = None
        self.ct = None
        self.pt = None


    def encrypt(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        cipher = Salsa20.new(key=self.key) # create instance of salsa20 class
        self.nonce=cipher.nonce

        start = timer()
        self.ct = self.nonce + cipher.encrypt(data) # 8byte nonce + data
        end = timer()
        return (end - start)

    def decrypt(self):
        
        cipher = Salsa20.new(key=self.key,nonce=self.nonce) # create instance of salsa20 class
        
        start = timer()
        self.pt=cipher.decrypt(self.ct[8:]) # parse ct. from 8th byte because first 8-bytes is nonce
        end = timer()
        return (end - start)

    def encryptTest(self,filepath):
        temp=0
        for i in range(20):
            temp+=self.encrypt(filepath)
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

