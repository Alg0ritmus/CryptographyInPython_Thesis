# Autor: Patrik Zeleňák
# Verzia: 0.1
# Poznámka: Následujúci kód bol vytvorený
# v rámci bakalárskej práce - Kryptografia v Pythone

# import dynamickej kniznice rust_py_blake3 s vyuzitim aliasu "r"
# pri volaní funkcii z danej kniznice budeme vyuzivat tento alias 
import rust_py_blake3 as r
# import casovaca pre odmeranie rychlosti kodu
from timeit import default_timer as timer

# citanie suboru v binarnom mode
with open("test.txt","rb") as f:
    file = f.read()
    start = timer()
    # hasovanie suboru s vyuzitim paralelizmu (na vsetkych dostupnych vlaknach)
    # pri volani funkcie pouzijeme alias "r"
    hash_data = r.rustypy_blake_parallel(file)

    end = timer()
print(bytes(hash_data).hex(),"\n cas",end-start)