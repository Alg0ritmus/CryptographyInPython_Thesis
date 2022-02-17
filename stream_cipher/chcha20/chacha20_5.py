from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import os
from timeit import default_timer as timer

class chacha20:
    def __init__(self) -> None:
        self.key = os.urandom(32)
        self.nonce =  os.urandom(16)
        self.ct = None
        self.pt = None
    
    def encrypt(self,filename="../../test.txt"):
        with open(filename, "rb") as encrypted_file:
            data = encrypted_file.read()

        

        algo = algorithms.ChaCha20(self.key,self.nonce)
        cipher = Cipher(algo,mode=None)
        encryptor = cipher.encryptor()
        


        start = timer()
        self.ct = encryptor.update(data)
        end = timer()
        return (end - start)
    
    def decrypt(self,filename="../../test.txt"):
        algo = algorithms.ChaCha20(self.key,self.nonce)
        cipher = Cipher(algo,mode=None)
        decryptor = cipher.decryptor()
        
        start = timer()
        self.pt = decryptor.update(self.ct)
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


filepath_ = "text.txt"
myChaCHa = chacha20()

myChaCHa.encrypt(filepath_)
# print ciphertext, tag
print(myChaCHa.getCT())

myChaCHa.decrypt()
#print pt from decrypted ct
print(myChaCHa.getPT())