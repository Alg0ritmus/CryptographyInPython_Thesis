# Testovanie kryptografických algoritmov a protokolov
Testovanie kryptografických algoritmov a protokolov z kľadiska správnosti vykonávania kryptografických úkonov, možno pre moduly PyCryptodome a Cryptography vykonat pomocou automatizovaných jednotkových testov, ktoré sú podporované danými modulmi.

## Modul PyCryptodome
Modul PyCryptodome ponúka automatizované pretestovanie modulu, založené na porovnávaní testovacích vektorov. Jednotkove testy pre modul PyCryptodome je možné spustiť následujúcov postupnostou teminalových príkazov (v tomto prípade pre OS Windows):

1) `pip install pycryptodome-test-vectors` _(stiahnutie testovacích vektorov)_
2) `python -m Cryptodome.SelfTest` _(spustenie jednotkových testov)_

Podmienkou je samozrejme nainštalovaný modul PyCryptodome. Viac o jednotkových testoch pre modul PyCryptodome možno nájsť na linke: https://www.pycryptodome.org/en/latest/src/installation.html?highlight=test#installation 

## Modul Cryptography
Podobne ako modul PyCryptodome, aj modul Cryptography ponúka automatizované pretestovanie modulu, založené na porovnávaní testovacích vektorov. Samotné jednotkové testy možno spustiť následujúcov postupnostou teminalových príkazov (v tomto prípade pre OS Windows):

1) Stiahnúť zdrojový kód (github repozitár): https://github.com/pyca/cryptography 
2) Po stiahnutí repozitára nainštalujeme potrebné developerské balíčky (tie je možné potom odstrániť). Inštaláciu vykonáme v stiahnutom repozitári (adresár obsahuje potrebný súbor `dev-requirements.txt`) Inštalácia: `pip install -r dev-requirements.txt`.
3) Po nainštalovaní všetkých potrebných modulov je vhodné sa uistiť, či verzia nainštalovaného modulu Cryptography je aktuálna. Príkaz `pip install cryptography --upgrade` automaticky aktualizuje a nainštaluje najnovšiu verziu modulu Cryptography. <br>
    Resp. je možné nainštalovať konkrétnu verziu modulu: _1)_ odstranenie aktuálnej verzie modulu `pip uninstall Cryptography` _2._ nainštalovanie konkrétnej verzie modulu `pip install Cryptography==37.0.2`
5) `pytest` _(spustenie jednotkových testov, realizovane v adresári modulu - repozitár so súborom dev-requirements.txt)_ 
6) Poznamka: Niektoré testy môžu zlyhať, pretože určité funkciu už nie su podporované aktuálne najnovšou verziou modulu Cryptography 37.0.2 (súvisi to aj so závislostou od knižnice OpenSSL a štruktúry zdrojových kódov). 

Podmienkou je samozrejme nainštalovaný (ideálne najnovšia verzia) modul Cryptography. Viac o jednotkových testoch pre modul Cryptography možno nájsť na linke: https://cryptography.io/en/latest/development/getting-started/?highlight=pytest#running-tests


## Modul Hashlib
Kryptografický modul Hashlib nedisponuje automatizovanými jednotkovými testami, a preto som pre otestovanie tohto modulu pripravil sadu testovacích funkcií _(v súbore hashlib_test.py)_, ktoré je možné spustiť príkazom:

1) `py hashlib_test.py` resp. `python hashlib_test.py` 


> Všetky dostupné kódy sú súčasťou experimentálnej časti Bc. práce: Kryptografia v Pythone. Zároveň prehlasujem, že vsetky dostupné kódy som vytvoril sám.  
P.Z.

