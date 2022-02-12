from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import os
from timeit import default_timer as timer

class RSA_2048:
    def __init__(self) -> None:
        self.private_key = None
        self.public_key =  None
        self.ct = None
        self.pt = None
        self.exponent = 65537
        self.modulus = 2048
    
    def setKeys(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=self.exponent,
            key_size=self.modulus
        )
        self.public_key=self.private_key.public_key()


    def encrypt(self,msg):        
        start = timer()

        self.ct = self.public_key.encrypt(
            msg,
            padding.OAEP(
                mgf= padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        end = timer()
        return (end - start)
    
    def decrypt(self):
       
        
        start = timer()

        self.pt = self.private_key.decrypt(
           self.ct,
           padding.OAEP(
               mgf=padding.MGF1(algorithm=hashes.SHA256()),
               algorithm=hashes.SHA256(),
               label=None
            )
        )
        
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


data = b"text.txt"
myRSA_2048 = RSA_2048()
myRSA_2048.setKeys()

myRSA_2048.encrypt(data)
# print ciphertext, tag
print(myRSA_2048.getCT())

myRSA_2048.decrypt()
#print pt from decrypted ct
print(myRSA_2048.getPT())