# https://www.pycryptodome.org/en/latest/src/cipher/cast.html?highlight=CAST5
from Cryptodome.Cipher import CAST
from Cryptodome.Util.Padding import pad,unpad
import os
from timeit import default_timer as timer

class CAST_128:
    def __init__(self) -> None:
        self.key = os.urandom(16) # 128 bits
        self.nonce = None
        self.ct = None
        self.pt = None
        self.IV = None
        self.ctrIV = os.urandom(8)

    def encryptECB(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = CAST.new(self.key,CAST.MODE_ECB)
        start = timer()
        self.ct = cipher.encrypt(pad(data,CAST.block_size))
        end = timer()
        return (end-start)
    
    def decryptECB(self):
        cipher = CAST.new(self.key,CAST.MODE_ECB)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),CAST.block_size)
        end = timer()
        return (end-start)

    
    def encryptCBC(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = CAST.new(self.key,CAST.MODE_CBC)
        self.IV = cipher.iv
        start = timer()
        self.ct = cipher.encrypt(pad(data,CAST.block_size))
        end = timer()
        return (end-start)
    
    def decryptCBC(self):
        cipher = CAST.new(self.key,CAST.MODE_CBC,self.IV)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),CAST.block_size)
        end = timer()
        return (end-start)

    
    def encryptCTR(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = CAST.new(self.key,CAST.MODE_CTR,nonce=b'',initial_value=self.ctrIV)
        start = timer()
        self.ct = cipher.encrypt(data)
        end = timer()
        return (end-start)
    
    def decryptCTR(self):
        cipher = CAST.new(self.key,CAST.MODE_CTR,nonce=b'',initial_value=self.ctrIV)
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
myCAST = CAST_128()
cas = myCAST.encryptECB()# parameter metody encrypt berie subor

print("šifrovanie:",cas,"sec")

#myCAST.decryptECB()
#print(myCAST.getPT())





