REM Rychlostny test Symetricke prudove sifry (ARC4, ChaCha20, Salsa20)

python .\symetric_stream\arc4\arc4_1.py >> vysledky.txt
python .\symetric_stream\arc4\arc4_2.py >> vysledky.txt
python .\symetric_stream\chcha20\chacha20_1.py >> vysledky.txt
python .\symetric_stream\chcha20\chacha20_2.py >> vysledky.txt
python .\symetric_stream\chcha20\chacha20_3.py >> vysledky.txt
python .\symetric_stream\chcha20\chacha20_4.py >> vysledky.txt
python .\symetric_stream\salsa20\salsa20_1.py >> vysledky.txt

REM Rychlostny test symetricke blokove sifry (AES, 3DES, CAST5, BLOWFISH)

python .\symetric\AES\AES_1.py >> vysledky.txt
python .\symetric\AES\AES_2.py >> vysledky.txt
python .\symetric\3DES\TDES_1.py >> vysledky.txt
python .\symetric\3DES\TDES_2.py >> vysledky.txt
python .\symetric\CAST5\cast5_1.py >> vysledky.txt
python .\symetric\CAST5\cast5_2.py >> vysledky.txt
python .\symetric\Blowfish\blowfish_1.py >> vysledky.txt
python .\symetric\Blowfish\blowfish_2.py >> vysledky.txt

REM Rychlostny test asymetricke algo (DSA, ECDSA, RSA-OAEP) # TATO CAST TRVA DLHO (niekolko desaitok minut)
python .\asymetric\DSA\DSA_1.py >> vysledky.txt
python .\asymetric\DSA\DSA_2.py >> vysledky.txt
python .\asymetric\ECC\ECC_1.py >> vysledky.txt
python .\asymetric\ECC\ECC_2.py >> vysledky.txt
python .\asymetric\RSA_OAEP\RSA_1.py >> vysledky.txt
python .\asymetric\RSA_OAEP\RSA_2.py >> vysledky.txt

REM Rychlostny test hasovacie funkcie (Blake2, SHA2, SHA3)
python .\hash\BLAKE2\blake2_1.py >> vysledky.txt
python .\hash\BLAKE2\blake2_2.py >> vysledky.txt
python .\hash\BLAKE2\blake2_3.py >> vysledky.txt
python .\hash\SHA2\SHA2_1.py >> vysledky.txt
python .\hash\SHA2\SHA2_2.py >> vysledky.txt
python .\hash\SHA2\SHA2_3.py >> vysledky.txt
python .\hash\SHA3\SHA3_1.py >> vysledky.txt
python .\hash\SHA3\SHA3_2.py >> vysledky.txt
python .\hash\SHA3\SHA3_3.py >> vysledky.txt