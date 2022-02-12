from time import time
from tracemalloc import start
from Cryptodome.Cipher import  ChaCha20_Poly1305
import base64
import os
from timeit import default_timer as timer


class chacha20:
    def __init__(self) -> None:
        self.key = os.urandom(32)
        self.nonce = os.urandom(12)
        self.aad = b'clear AAD data'
        self.ct = None
        self.pt =  None

    def encrypt(self,filename="../../test.txt"):
        with open(filename, "rb") as encrypted_file:
            data = encrypted_file.read()

        

        data = b'moje data'

        chacha = ChaCha20_Poly1305.new(key=self.key,nonce=self.nonce)
        

        start = timer()
        chacha.update(self.aad)
        self.ct = chacha.encrypt_and_digest(data)
        end = timer()

        return (end - start)

    def decrypt(self):
        chacha = ChaCha20_Poly1305.new(key=self.key,nonce=self.nonce)
        start= timer()
        chacha.update(self.aad)
        self.pt = chacha.decrypt_and_verify(self.ct[0],self.ct[1])
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

