# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/?highlight=RSA_OAEP#cryptography.hazmat.primitives.asymmetric.padding.OAEP
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import os
from timeit import default_timer as timer

class RSA_2048:
    def __init__(self,modulus=2048) -> None:
        self.private_key = None
        self.public_key =  None
        self.ct = None
        self.pt = None
        self.exponent = 65537
        self.modulus = modulus
    
    def setKeys(self):
        start = timer()
        self.private_key = rsa.generate_private_key(
            public_exponent=self.exponent,
            key_size=self.modulus
        )
        end = timer()
        self.public_key=self.private_key.public_key()
        return end-start

    def encrypt(self,msg):        
        start = timer()

        self.ct = self.public_key.encrypt(
            msg,
            padding.OAEP(
                mgf= padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        end = timer()
        return (end - start)
    
    def decrypt(self):
       
        
        start = timer()

        self.pt = self.private_key.decrypt(
           self.ct,
           padding.OAEP(
               mgf=padding.MGF1(algorithm=hashes.SHA256()),
               algorithm=hashes.SHA256(),
               label=None
            )
        )
        
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
print("\nModul: cryptography \nAlgoritmus: RSA_OAEP\n")

myRSA = RSA_2048(modulus=2048) # aktualne nastavene na modulus 2048 a vstupne data 190 B
print("Gen. kluca:",myRSA.setKeys(),"sec")
print("Sifrovanie dat (190MB), modulus = 2048:",myRSA.encrypt(os.urandom(190)),"sec")

myRSA = RSA_2048(modulus=4096) # aktualne nastavene na modulus 4096 a vstupne data 250 B
print("Gen. kluca:",myRSA.setKeys(),"sec")
print("Sifrovanie dat (250MB), modulus = 4096:",myRSA.encrypt(os.urandom(250)),"sec")

myRSA = RSA_2048(modulus=8192) # aktualne nastavene na modulus 8192 a vstupne data 500 B
print("Gen. kluca:",myRSA.setKeys(),"sec")
print("Sifrovanie dat (500MB), modulus = 8192:",myRSA.encrypt(os.urandom(500)),"sec")