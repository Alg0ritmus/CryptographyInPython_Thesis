import rustypyblake as r
from timeit import default_timer as timer


# https://pycryptodome.readthedocs.io/en/latest/src/hash/blake2s.html

class Hash:
    def __init__(self) -> None:
        self.result_from_rust = None
    
    def blake3_parallel(self,filepath="../../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        start= timer()
        self.result_from_rust = r.rustypy_blake_parallel(data)
        end=timer()
        
        return (end-start)
    
    def blake3(self,filepath="../../../test.txt"):
        with open(filepath, "rb") as encrypted_file:
            data = encrypted_file.read()
        start= timer()
        self.result_from_rust = r.rustypy_blake(data)
        end=timer()
        
        return (end-start)

    def hashTest(self,arg,filepath="../../../test.txt"):
        temp=0
        switch={
            "blake3": self.blake3,
            "blake3_parallel": self.blake3_parallel,
        }
        for i in range(20):
            temp+=switch[arg](filepath)
        print(temp/20)

    def getHexDigest(self):
        result=""
        for i in self.result_from_rust:
            result+=hex(i).lstrip("0x").rstrip("L")
        return result

data="text.txt"

myHash = Hash()
myHash.hashTest("blake3_parallel")
