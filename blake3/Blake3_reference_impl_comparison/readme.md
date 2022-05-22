# Testovanie rýchlosti referenčných impl. funkcie Blake3

Tento podadresár slúži na otestovanie všetkých 3 neoptimalizovaných referenčných implementácií hašovacej funkcie Blake3 (v jakyzu C, jazyku Pytho a v jazyku Rust).
<br>

## Testovanie:
1) Prvým krokom k otestovaniu daných implementácií je extrahovanie testovacích súborov (10MB, 20MB, 50MB) zo súboru _test_files.zip_. Testovacie súbory je nutné extrahovať do lokalného priečinka (priečinok, v ktorom sa nachádza daný ZIP súbor).

2) Samotný test vykonáme spustením súboru reference_test.bat. Referenčné implementácie sú mierne upravené, resp. použité tak aby brali parametre na štandardný vstup (vid .bat subor) a na štandardný výstup dávali dáta vo vhodnom formáte.

3) Výsledky (časy) vykonaných meraní budú dostupné v súbore _vysledky.txt_, ktorý bude automatický vytvorený pri spustení .bat súboru.

<br>

> Poznámka 1: Testovanie je nutné realizovať na OS Windows (.bat súbor).

> Poznámka 2: Testy boli napísane na následujúcich verziách pouzitých nástrojov: Rust - 1.56.1 | Python - 3.8.10 | GCC - 11.2.0 (MinGW-W64).