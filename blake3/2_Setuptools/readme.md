# Vytvorenie Python kniznice pre Rust modul Blake3 nástrojom setup-tools
Tento podadresár obsahuje zdrojové kódy potrebné pre vytvorenie python knižnice s využitím nástroja setup-tools a zároveň aj testovaciu demonštračnú aplikáciu pre odhašovanie súboru test.txt. V adresári _rust\_py\_blake3_ je vytvorená kompletná štruktúra potrebná pre využitie nástroja setup-tools. Kompletný návod pre tvorbu takejto štruktúry je možné nájsť v bc. práci. 

Pred samotným využitím nástroja setup-tools je potrebné nainštalovať niekoľko Python modulov:
1) `pip install setuptools-rust`
2) `pip install setuptools`
3) `pip install wheel`

Po nainštalovaní poterbných modulov môžeme začať s budovaním Python knižnice z Rust modulu Blake3 (Windows 10):  
1) Presunieme sa do adresára `rust_py_blake3`.
2) Príkazom `cargo build --release` vytvoríme prepájaci modul jazyka Rust
3) Príkazom `py setup.py install` vytvoríme Python knižnicu rust_py_blake3
4) Spustenie demo aplikácie je možné vykonať __bez__ potreby virtuálneho prostredia príkazom `py test.py` 

Vytvorená dynamická knižnica nie je parametrizovateľná z hľadiska počtu využívaných vlákien pre paralizovateľné hašovanie dát. V prípade využitia paralelizmu (funkcia __rustypy_blake_parallel()__) sa dáta automaticky spracujú všetkými dostupnými vláknami procesora.

Mapovanie Rust kódu s jazykom Python využíva Rust modul PyO3. Samotné mapovanie sa nachádza v súbore _src/lib.rs_.