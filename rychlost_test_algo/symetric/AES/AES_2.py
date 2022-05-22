# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://www.pycryptodome.org/en/latest/src/cipher/aes.html?highlight=AES
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
import os
from timeit import default_timer as timer

class AES_128:
    def __init__(self) -> None:
        self.key = os.urandom(16) # 128 bits
        self.nonce = None
        self.ct = None
        self.pt = None
        self.IV = None

    def encryptECB(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = AES.new(self.key,AES.MODE_ECB)
        start = timer()
        self.ct = cipher.encrypt(pad(data,AES.block_size))
        end = timer()
        return (end-start)
    
    def decryptECB(self):
        cipher = AES.new(self.key,AES.MODE_ECB)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),AES.block_size)
        end = timer()
        return (end-start)

    
    def encryptCBC(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = AES.new(self.key,AES.MODE_CBC)
        self.IV = cipher.iv
        start = timer()
        self.ct = cipher.encrypt(pad(data,AES.block_size))
        end = timer()
        return (end-start)
    
    def decryptCBC(self):
        cipher = AES.new(self.key,AES.MODE_CBC,self.IV)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),AES.block_size)
        end = timer()
        return (end-start)

    
    def encryptCTR(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = AES.new(self.key,AES.MODE_CTR)
        self.nonce = cipher.nonce
        start = timer()
        self.ct = cipher.encrypt(data)
        end = timer()
        return (end-start)
    
    def decryptCTR(self):
        cipher = AES.new(self.key,AES.MODE_CTR,nonce=self.nonce)
        start = timer()
        self.pt = cipher.decrypt(self.ct)
        end = timer()
        return (end-start)

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

print("\nModul: PyCryptodome \nAlgoritmus: AES_128-ECB\n" + "spracovanie 100MB suboru:",myAES.encryptECB(filepath=filepath_),"sec")
print("\nModul: PyCryptodome \nAlgoritmus: AES_128-CBC\n" + "spracovanie 100MB suboru:",myAES.encryptCBC(filepath=filepath_),"sec")
print("\nModul: PyCryptodome \nAlgoritmus: AES_128-CTR\n" + "spracovanie 100MB suboru:",myAES.encryptCTR(filepath=filepath_),"sec")


#myAES.decryptECB()
#print(myAES.getPT())

