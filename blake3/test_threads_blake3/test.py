# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

import rust_py_blake3 as r
from timeit import default_timer as timer
import sys

# citanie stdin parametrov a citanie suboru v bin tvare
threads=int(sys.argv[-1])
filename=sys.argv[-2]
f = open(filename,"rb")
file = f.read()
f.close()


start = timer()
# paralelne hasovanie dát s vyuzitim parametra threads (pocet vlakien) 
hash_data=r.rustypy_blake_parallel(file,threads)
end = timer()
print("\nModul: rust_py_blake3 \nAlgoritmus: Blake3")
print("Subor:",filename,"\nPocet vlakien:",threads,"\nhash:",bytes(hash_data).hex(),"\ncas:",(end-start),"sec")

