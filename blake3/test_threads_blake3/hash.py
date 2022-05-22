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
f = open("test.txt","rb") # zadaj názov súboru (testovacie subory su dostupne v test_files.zip)
file = f.read()
f.close()
# pocet vlakien, ktore chceme vyuzit
threads=4

start = timer()
# hasovanie suboru s poctom vlakien definovanych v premennej threads
hash_data=r.rustypy_blake_parallel(file,threads)
end = timer()
print(threads,"|| time:",(end-start))