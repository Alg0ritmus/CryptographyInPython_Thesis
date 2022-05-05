# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/?highlight=DES#cryptography.hazmat.primitives.ciphers.algorithms.TripleDES
from tracemalloc import start
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
from timeit import default_timer as timer

class TDES_128:
    def __init__(self) -> None:
        self.key = os.urandom(16)
        self.iv = os.urandom(8)
        self.nonce = os.urandom(8)
        self.ct = None
        self.pt = None

    def encryptECB(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        #implement TripleDES
        encryptor = Cipher(
            algorithms.TripleDES(self.key),
            modes.ECB(),
            backend=default_backend()
        ).encryptor()

        start = timer()
        self.ct = encryptor.update(self.pad(data)) + encryptor.finalize()
        end = timer()
        return (end-start)
    
    def decryptECB(self):
        #implement TripleDES
        decryptor = Cipher(
            algorithms.TripleDES(self.key),
            modes.ECB(),
            backend=default_backend()
        ).decryptor()

        start = timer()
        self.pt = self.unpad(decryptor.update(self.ct) + decryptor.finalize())
        end = timer()
        return (end-start)
    

    def encryptCBC(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        #implement TripleDES
        encryptor = Cipher(
            algorithms.TripleDES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        ).encryptor()

        start = timer()
        self.ct = encryptor.update(self.pad(data)) + encryptor.finalize()
        end = timer()
        return (end-start)
    
    def decryptCBC(self):
        #implement TripleDES
        decryptor = Cipher(
            algorithms.TripleDES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        ).decryptor()

        start = timer()
        self.pt = self.unpad(decryptor.update(self.ct) + decryptor.finalize())
        end = timer()
        return (end-start)
    
    def pad(self,data):
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data)

        padded_data += padder.finalize()
        return padded_data
    
    def unpad(self,data):
        unpadder =  padding.PKCS7(128).unpadder()
        data = unpadder.update(data)
        data += unpadder.finalize()
        return data

    def encryptTest(self,arg):
        temp=0
        switch={
            "ECB": self.encryptECB(),
            "CBC": self.encryptCBC()
        }
        for i in range(20):
            temp+=switch[arg]
        print(temp/20)
    
    def getPT(self):
        return self.pt

    def getCT(self):
        return self.ct


   
# RYCHLOSTNY TEST #
filepath_ = "text.txt" # tu je mozne zmenit PT(plain-text) subor
myTDES_128 = TDES_128()

print("šifrovanie:",myTDES_128.encryptECB(filepath_),"sec")
#print(myTDES_128.getCT()) #výpis šifry

#myTDES_128.decryptECB()
#print(myTDES_128.getPT())

