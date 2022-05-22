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
f = open("test.txt","rb")
file = f.read()

start = timer()
# hasovanie suboru bez vyuzitia paralelizmu (na 1 vlakne)
# pri volani funkcie pouzijeme alias "r"
hash_data = r.rustypy_blake(file)
end = timer()

timeS=end-start
print(bytes(hash_data).hex(),"\n cas",timeS)


start = timer()
# hasovanie suboru s vyuzitim paralelizmu (na vsetkych dostupnych vlaknach)
# pri volani funkcie pouzijeme alias "r"
hash_data = r.rustypy_blake_parallel(file)
end = timer()

timeS=end-start
print(bytes(hash_data).hex(),"\n cas par",timeS)