# Prepojenie externého Rust modulu Blake3 s jazykom Python, tvorba a test dynamickej python knižnice
Tento adresár obsahuje niekoľko podadresárov, ktoré sú zamerané na demonštráciu prepojenia externého Rust modulu Blake3 s jazykom Python, rôznými spôsobmi.

## Podadresár 1_Maturin
V tomto podadresári nájdeme zdrojové kódy potrebné na vytvorenie a otestovanie dynamického python modulu (Rust modul Blake3) s využitím nástroja maturin. Podadresár taktiež obsahuje demonštračnú aplikáciu, ktorá slúži na otestovanie funkčnosti dynamického Python modulu. 

## Podadresár 2_Setuptools
V tomto podadresári nájdeme zdrojové kódy potrebné na vytvorenie a otestovanie dynamického python modulu (Rust modul Blake3) s využitím nástroja setup-tools. Podadresár taktiež obsahuje demonštračnú aplikáciu, ktorá slúži na otestovanie funkčnosti dynamického Python modulu. 

## Podadresár 3_Manual
V tomto podadresári nájdeme zdrojové kódy potrebné na vytvorenie a otestovanie dynamického python modulu (Rust modul Blake3) manuálnym spôsobom. Podadresár taktiež obsahuje demonštračnú aplikáciu, ktorá slúži na otestovanie funkčnosti dynamického Python modulu. 

## Podadresár demo_pyd
Podadresár demo_pyd slúži čítateľovi na priame využitie a otestovanie dynamickej python knižnice. Podadresár obsahuje demonštračnú aplikáciu, pomocou ktorej je možné odhašovať súbor hašovacou funkciou Blake3.

## Podadresár test_threads_blake3
Podadresár test_threads_blake3 slúži podobne ako podadresár 3_Manual na vytvorenie a otestovanie python dynamického modulu (z Rust modulu Blake3) s možnosťou aktivácie ľubovoĽného počtu vákien procesora. Podadresár obsahuje demonštračnú aplikáciu, ktorou je možné hašovanie otestovať.

> Všetky dostupné kódy sú súčasťou experimentálnej časti Bc. práce: Kryptografia v Pythone. Zároveň prehlasujem, že vsetky dostupné kódy som vytvoril sám.  
P.Z.