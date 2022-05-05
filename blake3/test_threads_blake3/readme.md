# Otestovanie hašovacej funkcie Blake3 na ľubovoľnom počte vlákien CPU
Tento podadresár obsahuje zdrojové kódy potrebné pre vytvorenie python knižnice a otestovanie hašovacej funkcie Blake3 na ľubovoľnom počte vlákien CPU manuálnym spôsobom. Adresár zároveŇ poskytuje dynamickú Python knižnicu, ktorá je dostupná pre čítateľov, ktorí chcú iba otestovať hašovanie dát funkciou Blake3 (s ľobovoĽným počnom vlákien CPU jednotky). 

## Vytvorenie dynamického Python modulu je možné vykonať následovne (Windows 10):  
1) Presunieme sa do adresára `rust_py_blake3`.
2) Príkazom `cargo build --release` vytvoríme prepájaci modul jazyka Rust.
3) Skopírujeme súbor `rust_py_blake3.dll` z adresára `rust_py_blake3/target/release`.
4) Následne súbor `rust_py_blake3.dll` vložíme do adresára s demo aplikáciou (test.py).
5) Posledným krokom je prepísanie súboru `rust_py_blake3.dll` na `rust_py_blake3.pyd`.
6) Spustenie demo aplikácie je možné pomocou príkazu `py test.py`.

V prípade iného OS ako Windows, je možné postupovať podľa návodu v bc. práci.

## Využitie dynamickej Python knižnice (Windows 10):  
1) Spustenie demo aplikácie je možné pomocou príkazu `py test.py`.
Je nutné poznamenať, že dynamický pytjon modul rust_py_blake3.pyd sa musí nachádzať v rovnakom adresári ako demo aplikácia test.py.
V demonštračnej aplikácii je možné parametrizovať počet aktívných vlákien pri hašovaní súboru. 

> Všetky dostupné kódy sú súčasťou experimentálnej časti Bc. práce: Kryptografia v Pythone. Zároveň prehlasujem, že vsetky dostupné kódy som vytvoril sám.  
P.Z.