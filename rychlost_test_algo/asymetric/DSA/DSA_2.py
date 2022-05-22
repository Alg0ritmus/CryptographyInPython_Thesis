# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

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

f = open("test.txt","rb")
file100 = f.read()
f.close()

f = open("test2.txt","rb")
file200 = f.read()
f.close()

f = open("test3.txt","rb")
file1000 = f.read()
f.close()

print("\nModul: cryptography \nAlgoritmus: DSA\n")

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