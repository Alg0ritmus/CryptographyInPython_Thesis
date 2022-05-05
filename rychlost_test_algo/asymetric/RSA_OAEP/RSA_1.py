# https://www.pycryptodome.org/en/latest/src/cipher/oaep.html?highlight=OAEP
from time import time
from tracemalloc import start
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Util.Padding import pad,unpad
from Cryptodome.Random import get_random_bytes
import os
from timeit import default_timer as timer


class RSA_2048:
    def __init__(self) -> None:
        self.modulus = 2048
        self.public_key = None
        self.private_key = None
        self.ct = None
        self.pt = None

    
    def setKeys(self):
        start=timer()
        key = RSA.generate(self.modulus)
        end=timer()
        private_key = key.exportKey()
        with open("./private.pem", "wb") as f:
            f.write(private_key)

        public_key = key.publickey().exportKey()
        with open("receiver.pem", "wb") as f:
            f.write(public_key)
        return end-start

    def encrypt(self):
        recipient_key = RSA.import_key(open("./receiver.pem").read())
        session_key = get_random_bytes(190) # data na sifrovanie mensie nez key-size
        
        # Encrypt the session key with the public RSA key

        # LIMITATION => PT SHOULD BE SMALLER THAN KEY-SIZE
        cipher = PKCS1_OAEP.new(recipient_key)
        

        start = timer()
        self.ct = cipher.encrypt(session_key)
        end = timer()
        return (end-start)
    
    def decrypt(self):
        private_key = RSA.import_key(open("private.pem").read())
        cipher = PKCS1_OAEP.new(private_key)
        session_key = cipher.decrypt(self.ct)

        start = timer()
        self.pt = cipher.decrypt(self.ct)
        end = timer()
        return (end-start)
    
    
    def encryptTest(self,data):
        temp=0
        for i in range(20):
            self.setKeys()
            temp+=self.encrypt()
        print(temp/20)
    
    def getPT(self):
        return self.pt

    def getCT(self):
        return self.ct

    def getPublicKey(self):
        return self.public_key
    
    def getPrivateKey(self):
        return self.private_key
    


# RYCHLOSTNY TEST #
myRSA = RSA_2048() # aktualne nastavene na modulus 2048 a vstupne data 190 B
print("Gen. kluca:",myRSA.setKeys(),"sec")
print("Sifrovanie:",myRSA.encrypt(),"sec")
