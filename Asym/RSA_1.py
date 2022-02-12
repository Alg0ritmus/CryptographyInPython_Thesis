from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Util.Padding import pad,unpad
from Cryptodome.Random import get_random_bytes
import os
from timeit import default_timer as timer

# https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-rsa

class RSA_2048:
    def __init__(self) -> None:
        self.modulus = 2048
        self.public_key = None
        self.private_key = None
        self.ct = None
        self.pt = None

    
    def setKeys(self):
        key = RSA.generate(self.modulus)
        private_key = key.exportKey()
        with open("./private.pem", "wb") as f:
            f.write(private_key)

        public_key = key.publickey().exportKey()
        with open("receiver.pem", "wb") as f:
            f.write(public_key)

    def encrypt(self):
        recipient_key = RSA.import_key(open("./receiver.pem").read())
        session_key = get_random_bytes(16) # data na sifrovanie
        print("session_key",session_key)

        # Encrypt the session key with the public RSA key
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
    

#   EXAMPLE:
data = get_random_bytes(16)
myRSA = RSA_2048()
myRSA.setKeys()

myRSA.encrypt()
print(myRSA.getCT())

myRSA.decrypt()
print(myRSA.getPT())

