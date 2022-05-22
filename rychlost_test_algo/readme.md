# Testovanie kryptografických knižnic z hľadiska rýchlosti vykonávania algoritmov

V tomto podadresári sú vytvorené demonštračné aplikácie, ktoré majú za úlohu poskytnúť čítateľovi jeden zo spôsobov, ktorým je možné využiť dané kryptografické knižnice. V rámci bc. práce boli dané kryptografické Python knižnice testované z hľadiska rýchlosti vykonávania kryptografických algoritmov. Daný podadresár obsahuje aj súbor, ktorým je možné spustiť testy.

## Testovanie:
1) Prvým krokom k otestovaniu daných kryptografických knižnic pre jazyk Python je extrahovanie testovacích súborov (celkovo približne 5,5 GB) zo súboru _test_files.zip_. Testovacie súbory je nutné extrahovať do lokalného priečinka (priečinok, v ktorom sa nachádza daný ZIP súbor).

2) Samotný test vykonáme spustením súboru test_algo.bat. Referenčné implementácie sú mierne upravené, resp. použité tak aby brali parametre na štandardný vstup (vid .bat subor) a na štandardný výstup dávali dáta vo vhodnom formáte.

3) Výsledky (časy) vykonaných meraní budú dostupné v súbore _vysledky.txt_, ktorý bude automatický vytvorený pri spustení .bat súboru.

<br>

> Poznámka 2: Testy boli napísane na následujúcich verziách pouzitých nástrojov:  Python - 3.8.10 | modul - Cryptography 37.0.1 | modul - PyCryptodome 3.14.1 | modul - hashlib (PY verzia 3.8.10)