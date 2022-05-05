# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dsa/?highlight=DSA
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from timeit import default_timer as timer

class DSAalgo:
    def __init__(self):
        self.key_size = 3072
        self.private_key = b"",
        sepublic_key=b"",
        self.signature=b""
    
    def genKey(self):     
        self.private_key = dsa.generate_private_key(
            key_size=self.key_size,
        )
        
    
    def sign(self,data):
        self.signature = self.private_key.sign(
            data,
            hashes.SHA256()
        )


    def verify(self,data):
        self.public_key = self.private_key.public_key()
        self.public_key.verify(
            self.signature,
            data,
            hashes.SHA256()
        )
        

# RYCHLOSTNY TEST #

""" f = open("path_to_file.txt","rb")
file = f.read()
f.close()
"""
myDSA = DSAalgo()
start = timer()
myDSA.genKey()
end = timer()
print("Gen. kluca:",(end-start),"sec") 

start = timer()
myDSA.sign(b"sign this msg") # parameter v tejto casi mozeme nahradit suborom "file"
end = timer()
print("Dig. podpis:",(end-start),"sec") 
myDSA.verify(b"sign this msg")
#myDSA.verify(b"sign this msg")