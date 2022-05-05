import rust_py_blake3 as r
from timeit import default_timer as timer

f = open("test.txt","rb")
file = f.read()
threads=4

start = timer()
hash_data=r.rustypy_blake_parallel(file,threads)
end = timer()
print(threads,"|| time:",(end-start))

