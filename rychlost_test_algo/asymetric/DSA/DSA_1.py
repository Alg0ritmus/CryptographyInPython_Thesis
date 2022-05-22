# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# https://www.pycryptodome.org/en/latest/src/signature/dsa.html?highlight=DSA
from audioop import avg
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

f = open("test.txt","rb")
file100 = f.read()
f.close()

f = open("test2.txt","rb")
file200 = f.read()
f.close()

f = open("test3.txt","rb")
file1000 = f.read()
f.close()

print("\nModul: PyCryptodome \nAlgoritmus: DSA\n")

myDSA = DSAalgo()
test_array=[]
for i in range(100):
    start = timer()
    myDSA.genKey()
    end = timer()
    test_array.append(end-start)
print("Gen. kluca:\n max:",max(test_array),"\n min:",min(test_array),"\n avg:",sum(test_array)/100,"sec") 

start = timer()
myDSA.sign(file100) 
end = timer()
print("Dig. podpis 100MB suboru:",(end-start),"sec") 

start = timer()
myDSA.sign(file200) 
end = timer()
print("Dig. podpis 200MB suboru:",(end-start),"sec") 

start = timer()
myDSA.sign(file1000) 
end = timer()
print("Dig. podpis 1GB suboru:",(end-start),"sec") 

#myDSA.verify(b"sign this msg")
#myDSA.verify(b"sign this msg")
