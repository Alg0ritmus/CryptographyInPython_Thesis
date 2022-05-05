import rust_py_blake3 as r
from timeit import default_timer as timer

with open("test.txt","rb") as f:
    file = f.read()
    start = timer()

    hash_data = r.rustypy_blake_parallel(file)

    end = timer()
print(bytes(hash_data).hex(),"\n cas",end-start)