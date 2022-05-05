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

""" f = open("path_to_file.txt","rb")
file = f.read()
f.close()
"""
myECC = ECDSA()
start = timer()
myECC.genKey()
end = timer()
print("Gen. kluca:",(end-start),"sec") 

start = timer()
myECC.sign(b"sign this msg") # parameter v tejto casi mozeme nahradit suborom "file"
end = timer()
print("Dig. podpis:",(end-start),"sec") 
myECC.verify(b"sign this msg") # ak nevypise ziadnu chybu, overenie prebehlo uspesne
#myDSA.verify(b"sign this msg")