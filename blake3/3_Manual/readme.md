# Vytvorenie Python kniznice pre Rust modul Blake3 manuálnym spôsobom
Tento podadresár obsahuje zdrojové kódy potrebné pre vytvorenie python knižnice s manuálnym spôsobom a zároveň aj testovaciu demonštračnú aplikáciu pre odhašovanie súboru test.txt. 

Vytvorenie dynamického Python modulu je možné vykonať následovne (Windows 10):  
1) Presunieme sa do adresára `rust_py_blake3`.
2) Príkazom `cargo build --release` vytvoríme prepájaci modul jazyka Rust.
3) Skopírujeme súbor `rust_py_blake3.dll` z adresára `rust_py_blake3/target/release`.
4) Následne súbor `rust_py_blake3.dll` vložíme do adresára s demo aplikáciou (test.py).
5) Posledným krokom je prepísanie súboru `rust_py_blake3.dll` na `rust_py_blake3.pyd`.
6) Spustenie demo aplikácie je možné pomocou príkazu `py test.py`.

V prípade iného OS ako Windows, je možné postupovať podľa návodu v bc. práci.

Vytvorená dynamická knižnica nie je parametrizovateľná z hľadiska počtu využívaných vlákien pre paralizovateľné hašovanie dát. V prípade využitia paralelizmu (funkcia __rustypy_blake_parallel()__) sa dáta automaticky spracujú všetkými dostupnými vláknami procesora.

Mapovanie Rust kódu s jazykom Python využíva Rust modul PyO3. Samotné mapovanie sa nachádza v súbore _src/lib.rs_.