# https://www.pycryptodome.org/en/latest/src/signature/dsa.html?highlight=DSA
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import DSA
from Cryptodome.Signature import DSS
from timeit import default_timer as timer

class DSAalgo:
    def __init__(self):
        self.size=3072
        self.key = b''
        self.signature = b''
        

# KEY GEN
    def genKey(self):
        self.key = DSA.generate(self.size)
        f = open("public_key.pem", "wb")
        f.write(self.key.publickey().export_key())
        f.close()


# SIGN
    def sign(self,message):
        hash_obj = SHA256.new(message)
        signer = DSS.new(self.key, 'fips-186-3')
        self.signature = signer.sign(hash_obj)


# VERIFY
    def verify(self,data):
        f = open("public_key.pem", "rb")
        hash_obj = SHA256.new(data)
        pub_key = DSA.import_key(f.read())
        verifier = DSS.new(pub_key, 'fips-186-3')
        try:
            verifier.verify(hash_obj, self.signature)
            print( "The message is authentic.")
        except ValueError:
            print( "The message is not authentic.") 


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