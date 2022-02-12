import os
from chacha20poly1305 import ChaCha20Poly1305
from timeit import default_timer as timer

# Implementation:
# https://github.com/ph4r05/py-chacha20poly1305
#
# Not recommended implementation
class chacha20:
	def __init__(self) -> None:
		self.key = os.urandom(32)
		self.nonce = os.urandom(12)
		self.ct = None
		self.pt = None

	def encrypt(self,filename="../../test.txt"):
		with open(filename, "rb") as encrypted_file:
			data = encrypted_file.read()


		cip = ChaCha20Poly1305(self.key)

		start = timer()
		self.ct = cip.encrypt(self.nonce, data)
		end = timer()
		return (end - start)

	def decrypt(self):
		cip = ChaCha20Poly1305(self.key)

		start = timer()
		self.pt = cip.decrypt(self.nonce, self.ct)
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


filepath_ = "text.txt"
myChaCHa = chacha20()

myChaCHa.encrypt(filepath_)
# print ciphertext, tag
print(myChaCHa.getCT())

myChaCHa.decrypt()
#print pt from decrypted ct
print(myChaCHa.getPT())

