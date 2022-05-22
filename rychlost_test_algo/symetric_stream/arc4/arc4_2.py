# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

#https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
import os
from timeit import default_timer as timer
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Arc4:
    def __init__(self) -> None:
        self.key=os.urandom(16)
        self.ct = None
        self.pt = None


    def encrypt(self,filepath='text.txt'):
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
    

# RYCHLOSTNY TEST #
filepath_ = "test.txt" # tu je mozne zmenit PT(plain-text) subor
myArc = Arc4()


print("\nModul: cryptography \nAlgoritmus: ARC4\n" + "spracovanie 100MB suboru:",myArc.encrypt(filepath_),"sec")
#print(myArc.getCT())

#myArc.decrypt()
#print(myArc.getPT())



