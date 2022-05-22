# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://www.pycryptodome.org/en/latest/src/cipher/blowfish.html?highlight=Blowfish
from Cryptodome.Cipher import Blowfish
from Cryptodome.Util.Padding import pad,unpad
import os
from timeit import default_timer as timer

class Blowfish_128:
    def __init__(self) -> None:
        self.key = os.urandom(16) # 128 bits
        self.ct = None
        self.pt = None
        self.IV = None
        self.ctrIV = os.urandom(8) # 64 bit nonce

    def encryptECB(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = Blowfish.new(self.key,Blowfish.MODE_ECB)
        start = timer()
        self.ct = cipher.encrypt(pad(data,Blowfish.block_size))
        end = timer()
        return (end-start)
    
    def decryptECB(self):
        cipher = Blowfish.new(self.key,Blowfish.MODE_ECB)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),Blowfish.block_size)
        end = timer()
        return (end-start)

    
    def encryptCBC(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = Blowfish.new(self.key,Blowfish.MODE_CBC)
        self.IV = cipher.iv
        start = timer()
        self.ct = cipher.encrypt(pad(data,Blowfish.block_size))
        end = timer()
        return (end-start)
    
    def decryptCBC(self):
        cipher = Blowfish.new(self.key,Blowfish.MODE_CBC,self.IV)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),Blowfish.block_size)
        end = timer()
        return (end-start)

    
    def encryptCTR(self,filepath='../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = Blowfish.new(self.key,Blowfish.MODE_CTR,initial_value=self.ctrIV,nonce=b'')# nonce is fixed, so we do not need to change it -> docs
        start = timer()
        self.ct = cipher.encrypt(data)
        end = timer()
        return (end-start)
    
    def decryptCTR(self):
        cipher = Blowfish.new(self.key,Blowfish.MODE_CTR,initial_value=self.ctrIV,nonce=b'')
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
myBlowfish = Blowfish_128()

print("\nModul: PyCryptodome \nAlgoritmus: Blowfish_128-ECB\n" + "spracovanie 100MB suboru:",myBlowfish.encryptECB(filepath=filepath_),"sec")
print("\nModul: PyCryptodome \nAlgoritmus: Blowfish_128-CBC\n" + "spracovanie 100MB suboru:",myBlowfish.encryptCBC(filepath=filepath_),"sec")
print("\nModul: PyCryptodome \nAlgoritmus: Blowfish_128-CTR\n" + "spracovanie 100MB suboru:",myBlowfish.encryptCTR(filepath=filepath_),"sec")

#myBlowfish.decryptECB()
#print(myBlowfish.getPT())




