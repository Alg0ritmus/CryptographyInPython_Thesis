# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/
import encodings
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils
from timeit import default_timer as timer


class ECDSA:
    def __init__(self):
        private_key = b"",
        public_key=b"",
        signature=b""
    
    def genKey(self):     
        self.private_key = ec.generate_private_key(
            ec.SECP256R1()
        )
        self.public_key = self.private_key.public_key()
        
    
    def sign(self,data):
        self.signature = self.private_key.sign(
            data,
            ec.ECDSA(hashes.SHA256())
        )


    def verify(self,data):

        chosen_hash = hashes.SHA256()
        hasher = hashes.Hash(chosen_hash)
        hasher.update(data)
        digest = hasher.finalize()
        self.public_key.verify(
            self.signature,
            digest,
            ec.ECDSA(utils.Prehashed(chosen_hash))
        )


# RYCHLOSTNY TEST #

f = open("test.txt","rb")
file100 = f.read()
f.close()

f = open("test2.txt","rb")
file200 = f.read()
f.close()

f = open("test3.txt","rb")
file1000 = f.read()
f.close()

print("\nModul: cryptography \nAlgoritmus: ECDSA_3072-P256-SHA256\n")

myECC = ECDSA()
test_array=[]
for i in range(10):
    start = timer()
    myECC.genKey()
    end = timer()
    test_array.append(end-start)
print("Gen. kluca:\n max:",max(test_array),"\n min:",min(test_array),"\n avg:",sum(test_array)/100,"sec") 


start = timer()
myECC.sign(file100) 
end = timer()
print("Dig. podpis 100MB suboru:",(end-start),"sec") 

start = timer()
myECC.sign(file200) 
end = timer()
print("Dig. podpis 200MB suboru:",(end-start),"sec") 

start = timer()
myECC.sign(file1000) 
end = timer()
print("Dig. podpis 1GB suboru:",(end-start),"sec") 

""" 
start = timer()
myECC.sign(b"sign this msg") # parameter v tejto casi mozeme nahradit suborom "file"
end = timer()
print("Dig. podpis:",(end-start),"sec") 
myECC.verify(b"sign this msg") 
"""
#myDSA.verify(b"sign this msg")
