# Otestovanie hašovacej funkcie Blake3 na ľubovoľnom počte vlákien CPU
Tento podadresár obsahuje zdrojové kódy potrebné pre vytvorenie python knižnice a otestovanie hašovacej funkcie Blake3 na ľubovoľnom počte vlákien CPU manuálnym spôsobom. Adresár zároveň poskytuje dynamickú Python knižnicu, ktorá je dostupná pre čítateľov, ktorí chcú iba otestovať hašovanie dát funkciou Blake3 (s ľubovoľným počtom vlákien CPU jednotky). 

## Vytvorenie dynamického Python modulu je možné vykonať následovne (Windows 10):  
1) Presunieme sa do adresára `rust_py_blake3`.
2) Príkazom `cargo build --release` vytvoríme prepájaci modul jazyka Rust.
3) Skopírujeme súbor `rust_py_blake3.dll` z adresára `rust_py_blake3/target/release`.
4) Následne súbor `rust_py_blake3.dll` vložíme do adresára s demo aplikáciou (test.py).
5) Posledným krokom je prepísanie súboru `rust_py_blake3.dll` na `rust_py_blake3.pyd`.
6) Spustenie demo aplikácie je možné pomocou príkazu `py hash.py`. V súbore `py hash.py` je nutné nastaviť cestu k súboru, kt. chceme hašovať.

V prípade iného OS ako Windows, je možné postupovať podľa návodu v bc. práci.

## Využitie dynamickej Python knižnice (Windows 10):  
1) Spustenie demo aplikácie je možné pomocou príkazu `py hash.py`.
Je nutné poznamenať, že dynamický pytjon modul rust_py_blake3.pyd sa musí nachádzať v rovnakom adresári ako demo aplikácia test.py.
V demonštračnej aplikácii je možné parametrizovať počet aktívných vlákien pri hašovaní súboru. V súbore `py hash.py` je nutné nastaviť cestu k súboru, kt. chceme hašovať.

## Test rust_py_blake3 vs optimalizovaná. Rust impl na OS Windows.

Obe implementácie sú paralizovateľné (mierne modifikované pre využitie variabilného počtu vlákien). Patametrizácia funkcie pre Rust impl. bola realizovaná v súbore `blake3_opt_impl\src\main.rs` a pre impl rust_py_blake3 v súbore `rust_py_blake3\src\lib.rs`. Spustenie testu je možné vykonať následovne.

1) Prvým krokom k otestovaniu daných implementácií je extrahovanie testovacích súborov (100MB, 200MB, 1GB) zo súboru _test_files.zip_. Testovacie súbory je nutné extrahovať do lokalného priečinka (priečinok, v ktorom sa nachádza daný ZIP súbor).

2) Samotný test vykonáme spustením súboru test_threads.bat. Implementácie sú mierne upravené, resp. použité tak aby brali parametre na štandardný vstup (vid .bat subor) a na štandardný výstup dávali dáta vo vhodnom formáte.

3) Výsledky (časy) vykonaných meraní budú dostupné v súbore _vysledky.txt_, ktorý bude automatický vytvorený pri spustení .bat súboru.


<br>

> Poznámka 1: Testovanie je nutné realizovať na OS Windows (.bat súbor).

> Poznámka 2: Testy boli napísane na následujúcich verziách pouzitých nástrojov: Rust - 1.56.1 | Python - 3.8.10.