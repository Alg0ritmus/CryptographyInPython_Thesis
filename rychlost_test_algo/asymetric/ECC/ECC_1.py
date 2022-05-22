# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://www.pycryptodome.org/en/latest/src/signature/dsa.html?highlight=DSA
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import ECC
from Cryptodome.Signature import DSS
from timeit import default_timer as timer

class ECDSA:
    def __init__(self):
        self.curve=["P-192","P-224","P-256","P-384","P-521"][2]
        self.message = b''
        self.signature = b''
        

# KEY GEN
    def genKey(self):
        private_key = ECC.generate(curve=self.curve)

        f = open("private.pem", "wt")
        f.write(private_key.export_key(
            format="PEM",
            use_pkcs8=True,
            protection="PBKDF2WithHMAC-SHA1AndAES128-CBC",
        ))
        f.close()

        f = open("public.pem", "wt")
        f.write(private_key.public_key().export_key(format="PEM"))
        f.close()


# SIGN
    def sign(self,message):
        self.message = message
        key = ECC.import_key(open('private.pem').read())
        h = SHA256.new(message)
        signer = DSS.new(key, 'fips-186-3')
        self.signature = signer.sign(h)


# VERIFY
    def verify(self,data):
        received_message = data
        key = ECC.import_key(open('public.pem').read())
        h = SHA256.new(received_message)
        verifier = DSS.new(key, 'fips-186-3')
        try:
            verifier.verify(h, self.signature)
            print( "The message is authentic.")
        except ValueError:
            print( "The message is not authentic.") 

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

print("\nModul: PyCryptodome \nAlgoritmus: ECDSA_3072-P256-SHA256\n")

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

