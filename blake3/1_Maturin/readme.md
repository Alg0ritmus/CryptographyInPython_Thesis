# Vytvorenie dynamickej Python kniznice pre Rust modul Blake3 nástrojom maturin
Tento podadresár obsahuje zdrojové kódy potrebné pre vytvorenie dynamickej python knižnice s využitím nástroja maturin a zároveň aj testovaciu demonštračnú aplikáciu pre odhašovanie súboru test.txt.

Vytvoriť a otestovať dynamickú Python knižnicu možno následovne (Windows 10):  
1) Presunieme sa do adresára `rust_py_blake3`.
2) Príkazom `cargo build --release` vytvoríme prepájaci modul jazyka Rust
3) Príkazom `py -m venv .env` vytvoríme virtuálne prostredie jazyka Python
4) Príkazom `.\.env\Scripts\activate` spustíme virtuálne prostredie jazyka Python
5) `pip install maturin` je príkaz, ktorým nainštalujeme nástroj maturin do virtuálneho prostredia
6) Príkazom `maturin develop --release` vytvoríme dynamickú python knižnicu
7) Spustenie demo aplikácie je možné vykonať z __virtuálneho prostredia__ príkazom `py test.py` 

Vytvorená dynamická knižnica nie je parametrizovateľná z hľadiska počtu využívaných vlákien pre paralizovateľné hašovanie dát. V prípade využitia paralelizmu (funkcia __rustypy_blake_parallel()__) sa dáta automaticky spracujú všetkými dostupnými vláknami procesora.

Mapovanie Rust kódu s jazykom Python využíva Rust modul PyO3. Samotné mapovanie sa nachádza v súbore _src/lib.rs_.