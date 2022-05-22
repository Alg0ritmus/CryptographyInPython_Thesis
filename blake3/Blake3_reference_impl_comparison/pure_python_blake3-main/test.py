import os
import pure_blake3
from timeit import default_timer as timer
import sys

#print("stdin:", sys.argv[-1])

f = open(sys.argv[-1],"rb")
file = f.read()
#file = os.urandom(10*2**20)
hasher1 = pure_blake3.Hasher()

start = timer()
hasher1.update(file)
hash_data = hasher1.finalize()
end = timer()

#print(bytes(hash_data).hex(),"cas= ",end-start)
sys.stdout.write("PYTHON - "+str(sys.argv[-1])+"\n"+str(bytes(hash_data).hex())+"\nTime: "+str(end-start)+"\n")



