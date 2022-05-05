from cryptography.hazmat.primitives import hashes, hmac
from timeit import default_timer as timer

class MYHMAC:
    def __init__(self,signature):
        self.signature = signature

    def Update(self,key):
        h = hmac.HMAC(key, hashes.SHA256())
        h.update(b"message to hash")
        self.signature = h.finalize()

    def Verify(self,key):
        h = hmac.HMAC(key, hashes.SHA256())
        h.update(b"message to hash")
        h_copy = h.copy() # get a copy of `h' to be reused
        h.verify(self.signature)

# TEST #
start = timer()
myHMAC = MYHMAC(b"Test of HMAC")
myHMAC.Update(b"secretKey")
end = timer()
print("HMAC:",end-start,"sec")
#myHMAC.Verify(B'secretKey')