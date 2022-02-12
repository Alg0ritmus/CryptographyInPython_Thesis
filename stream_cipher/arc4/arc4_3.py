import os
from timeit import default_timer as timer
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

#https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/

class Arc4:
    def __init__(self) -> None:
        self.key=os.urandom(16)
        self.ct = None
        self.pt = None


    def encrypt(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        algorithm = algorithms.ARC4(self.key)
        cipher = Cipher(algorithm, mode=None)
        encryptor = cipher.encryptor()


        start = timer()
        self.ct = encryptor.update(data)
        end = timer()
        return (end - start)

    def decrypt(self):
        algorithm = algorithms.ARC4(self.key)
        cipher = Cipher(algorithm, mode=None)
        decryptor = cipher.decryptor()
        

        start = timer()
        self.pt=decryptor.update(self.ct)
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
    

#   EXAMPLE:
filepath_ = "text.txt"
myArc = Arc4()

myArc.encryptTest()



