# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

from Cryptodome.Hash import HMAC, SHA256
from timeit import default_timer as timer
class MYHMAC:
    def __init__(self,msg):
        self.msg = msg
        self.mac = b''

    def Update(self,key):
        h = HMAC.new(key, digestmod=SHA256)
        h.update(self.msg)
        self.mac=h.hexdigest()

    def Verify(self,key):
        h = HMAC.new(key, digestmod=SHA256)
        h.update(self.msg)
        try:
            h.hexverify(self.mac)
            print("The message '%s' is authentic" % self.msg)
        except ValueError:
            print("The message or the key is wrong")

# TEST #
start = timer()
myHMAC = MYHMAC(b"Test of HMAC")
myHMAC.Update(b"secretKey")
end = timer()
print("HMAC:",end-start,"sec")
#myHMAC.Verify(B'secretKey')
