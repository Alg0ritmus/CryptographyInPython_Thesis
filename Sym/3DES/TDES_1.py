from Cryptodome.Cipher import DES3
from Cryptodome.Util.Padding import pad,unpad
import os
from timeit import default_timer as timer

#https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ecb-mode

class TDES_128:
    def __init__(self) -> None:
        self.key = DES3.adjust_key_parity(os.urandom(24)) # 128 bits
        self.ct = None
        self.pt = None
        self.IV = None
        self.ctrIV = os.urandom(8) # 64 bit nonce

    def encryptECB(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = DES3.new(self.key,DES3.MODE_ECB)
        start = timer()
        self.ct = cipher.encrypt(pad(data,DES3.block_size))
        end = timer()
        return (end-start)
    
    def decryptECB(self):
        cipher = DES3.new(self.key,DES3.MODE_ECB)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),DES3.block_size)
        end = timer()
        return (end-start)

    
    def encryptCBC(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = DES3.new(self.key,DES3.MODE_CBC)
        self.IV = cipher.iv
        start = timer()
        self.ct = cipher.encrypt(pad(data,DES3.block_size))
        end = timer()
        return (end-start)
    
    def decryptCBC(self):
        cipher = DES3.new(self.key,DES3.MODE_CBC,self.IV)
        start = timer()
        self.pt = unpad(cipher.decrypt(self.ct),DES3.block_size)
        end = timer()
        return (end-start)

    
    def encryptCTR(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        
        cipher = DES3.new(self.key,DES3.MODE_CTR,initial_value=self.ctrIV,nonce=b'')# nonce is fixed, so we do not need to change it -> docs
        start = timer()
        self.ct = cipher.encrypt(data)
        end = timer()
        return (end-start)
    
    def decryptCTR(self):
        cipher = DES3.new(self.key,DES3.MODE_CTR,initial_value=self.ctrIV,nonce=b'')
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
    

#   EXAMPLE:
filepath_ = "text.txt"
myTDES_128 = TDES_128()

myTDES_128.encryptCTR(filepath_)
print(myTDES_128.getCT())

myTDES_128.decryptCTR()
print(myTDES_128.getPT())




