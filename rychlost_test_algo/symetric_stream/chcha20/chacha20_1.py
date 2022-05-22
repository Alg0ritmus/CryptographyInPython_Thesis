# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://cryptography.io/en/latest/hazmat/primitives/aead/?highlight=chacha20
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
from timeit import default_timer as timer



class chacha20:
    def __init__(self) -> None:
        self.key=os.urandom(32)
        self.nonce = os.urandom(12)
        self.aad = b"authenticated but unencrypted data also known as Additional authenticated data"
        self.ct = None
        self.pt = None


    def encrypt(self,filepath='text.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        chacha = ChaCha20Poly1305(self.key) # create instance of ChaCha20Poly1305 class
      

        start = timer()
        self.ct = chacha.encrypt(self.nonce, data, self.aad)
        end = timer()
        return (end - start)

    def decrypt(self):
        
        chacha = ChaCha20Poly1305(self.key) # create instance of ChaCha20Poly1305 class

        start = timer()
        self.pt=chacha.decrypt(self.nonce, self.ct, self.aad)
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
myChaCHa = chacha20()

print("\nModul: cryptography \nAlgoritmus: ChaCha20Poly1305\n" + "spracovanie 100MB suboru:",myChaCHa.encrypt(filepath_),"sec")
#print(myChaCHa.getCT())
#
#myChaCHa.decrypt()
#print(myChaCHa.getPT())


