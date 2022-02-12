import os
from timeit import default_timer as timer
from arc4 import ARC4

#https://pypi.org/project/arc4/

class Arc4:
    def __init__(self) -> None:
        self.key=os.urandom(16)
        self.ct = None
        self.pt = None


    def encrypt(self,filepath='../../test.txt'):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()

        arc4 = ARC4(self.key)

        start = timer()
        self.ct = arc4.encrypt(data)
        end = timer()
        return (end - start)

    def decrypt(self):
        
        arc4 = ARC4(self.key) # create instance of ARC4 class

        start = timer()
        self.pt=arc4.decrypt(self.ct)
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
    

#   EXAMPLE:
filepath_ = "text.txt"
myArc = Arc4()

myArc.encrypt(filepath_)
print(myArc.getCT())

myArc.decrypt()
print(myArc.getPT())



