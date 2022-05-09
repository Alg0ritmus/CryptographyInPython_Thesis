## Otestovanie dynamickej Python knižnice
V prípade, že čítateľ nemá v úmysle prepájať Rust modul Blake3 s jazykom Python ale chce otestovať hašovanie súborov pomocou funkcie Blake3 z jazyka Python, je možné využiť už vytvorenú dynamickú Python knižnicu. V tomto repozitári sa nachádza dynamická Python knižnica a demo aplikácia (test.py).

V testovacej demo aplikácii je naimportovaná dynamická Python knižnica (rust_py_blake3.pyd) a spustenie danej demo aplikácie je možné vykonať príkadom:
1) `py test.py`

Demonštračná aplikácie zahašuje dostupný testovací súbor test.txt.

> Všetky dostupné kódy sú súčasťou experimentálnej časti Bc. práce: Kryptografia v Pythone. Zároveň prehlasujem, že vsetky dostupné kódy som vytvoril sám.  
P.Z.
