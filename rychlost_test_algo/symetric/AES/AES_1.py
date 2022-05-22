# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
from timeit import default_timer as timer

class AES_128:
    def __init__(self) -> None:
        self.key = os.urandom(16)
        self.iv = os.urandom(16)
        self.nonce = os.urandom(16)
        self.ct = None
        self.pt = None

    def encryptECB(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        #implement AES
        encryptor = Cipher(
            algorithms.AES(self.key),
            modes.ECB(),
            backend=default_backend()
        ).encryptor()

        start = timer()
        self.ct = encryptor.update(self.pad(data)) + encryptor.finalize()
        end = timer()
        return (end-start)
    
    def decryptECB(self):
        #implement AES
        decryptor = Cipher(
            algorithms.AES(self.key),
            modes.ECB(),
            backend=default_backend()
        ).decryptor()

        start = timer()
        self.pt = self.unpad(decryptor.update(self.ct) + decryptor.finalize())
        end = timer()
        return (end-start)
    

    def encryptCBC(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        #implement AES
        encryptor = Cipher(
            algorithms.AES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        ).encryptor()

        start = timer()
        self.ct = encryptor.update(self.pad(data)) + encryptor.finalize()
        end = timer()
        return (end-start)
    
    def decryptCBC(self):
        #implement AES
        decryptor = Cipher(
            algorithms.AES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        ).decryptor()

        start = timer()
        self.pt = self.unpad(decryptor.update(self.ct) + decryptor.finalize())
        end = timer()
        return (end-start)


    def encryptCTR(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        #implement AES
        encryptor = Cipher(
            algorithms.AES(self.key),
            modes.CTR(self.nonce),
            backend=default_backend()
        ).encryptor()

        start = timer()
        self.ct = encryptor.update(data) + encryptor.finalize()
        end = timer()
        return (end-start)
    
    def decryptCTR(self):
        #implement AES
        decryptor = Cipher(
            algorithms.AES(self.key),
            modes.CTR(self.nonce),
            backend=default_backend()
        ).decryptor()

        start = timer()
        self.pt = decryptor.update(self.ct) + decryptor.finalize()
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
            "CBC": self.encryptCBC(),
            "CTR": self.encryptCTR()
        }
        for i in range(20):
            temp+=switch[arg]
        print(temp/20)
    
    def getPT(self):
        return self.pt

    def getCT(self):
        return self.ct


   


# RYCHLOSTNY TEST #
filepath_ = "test.txt" # tu je mozne zmenit PT(plain-text) subor
myAES = AES_128()

print("\nModul: cryptography \nAlgoritmus: AES_128-ECB\n" + "spracovanie 100MB suboru:",myAES.encryptECB(filepath=filepath_),"sec")
print("\nModul: cryptography \nAlgoritmus: AES_128-CBC\n" + "spracovanie 100MB suboru:",myAES.encryptCBC(filepath=filepath_),"sec")
print("\nModul: cryptography \nAlgoritmus: AES_128-CTR\n" + "spracovanie 100MB suboru:",myAES.encryptCTR(filepath=filepath_),"sec")

#myAES.decryptECB()
#print(myAES.getPT())

