# Prepojenie externého Rust modulu Blake3 s jazykom Python, tvorba a test dynamickej python knižnice
Tento adresár obsahuje niekoľko podadresárov, ktoré sú zamerané na demonštráciu prepojenia externého Rust modulu Blake3 s jazykom Python, rôznými spôsobmi.

```diff
-Varovanie: Všetky DLL knižnice pre jazyk Python (súbory s príponou .pyd) sú generované pre verziu Python 3.8.10. 
-Ak používaťe inú verziu Pythonu, je nutné vygenerovať nové DLL knižnice kompatibilné s vašou verziou Pythonu. 
-Pre vygenerovanie DLL knižnice `rusty_py_blake3.pyd` je nutné si vybrať jedenu z dostupných metód 
-(1_Maturin/2_Setuptools/3_Manual) a postupovať podľa uvedeného návodu.
```
__Poznámka: Pri generovaní DLL knižníc je potrebné mať nainštalovaný prog. jazyk <a href="https://www.rust-lang.org/tools/install">Rust.</a>__

## Podadresár 1_Maturin
V tomto podadresári nájdeme zdrojové kódy potrebné na vytvorenie a otestovanie dynamického python modulu (Rust modul Blake3) s využitím nástroja maturin. Podadresár taktiež obsahuje demonštračnú aplikáciu, ktorá slúži na otestovanie funkčnosti dynamického Python modulu. 

## Podadresár 2_Setuptools
V tomto podadresári nájdeme zdrojové kódy potrebné na vytvorenie a otestovanie dynamického python modulu (Rust modul Blake3) s využitím nástroja setup-tools. Podadresár taktiež obsahuje demonštračnú aplikáciu, ktorá slúži na otestovanie funkčnosti dynamického Python modulu. 

## Podadresár 3_Manual
V tomto podadresári nájdeme zdrojové kódy potrebné na vytvorenie a otestovanie dynamického python modulu (Rust modul Blake3) manuálnym spôsobom. Podadresár taktiež obsahuje demonštračnú aplikáciu, ktorá slúži na otestovanie funkčnosti dynamického Python modulu. 

## Podadresár Blake3_reference_impl_comparison
Obsahuje vsetky 3 referenčné implementácie (v jazyku C, Python, Rust), ktoré sú rýchlostne testované.

## Podadresár demo_pyd
Podadresár demo_pyd slúži čítateľovi na priame využitie a otestovanie dynamickej python knižnice. Podadresár obsahuje demonštračnú aplikáciu, pomocou ktorej je možné odhašovať súbor hašovacou funkciou Blake3.

## Podadresár test_threads_blake3
Podadresár test_threads_blake3 slúži podobne ako podadresár 3_Manual na vytvorenie a otestovanie python dynamického modulu (z Rust modulu Blake3) s možnosťou aktivácie ľubovoĽného počtu vákien procesora. Podadresár obsahuje demonštračnú aplikáciu, ktorou je možné hašovanie otestovať.

