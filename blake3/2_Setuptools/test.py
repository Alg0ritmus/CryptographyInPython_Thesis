import rust_py_blake3 as r
from timeit import default_timer as timer

f = open("test.txt","rb")
file = f.read()

start = timer()
hash_data = r.rustypy_blake(file)
end = timer()

timeS=end-start
print(bytes(hash_data).hex(),"\n cas",timeS)


start = timer()
hash_data = r.rustypy_blake_parallel(file)
end = timer()

timeS=end-start
print(bytes(hash_data).hex(),"\n cas par",timeS)