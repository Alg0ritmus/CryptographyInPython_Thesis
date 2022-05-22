REM Preklad C-suborov
gcc .\blake3_reference_impl_c-main\reference_impl.c .\blake3_reference_impl_c-main\main.c -o .\blake3_reference_impl_c-main\blake3
REM Preklad Rust-suborov
cd .\reference_impl
cargo build --release
cd ..

REM C: HASOVANIE 10MB SUBORU, POMOCOU REF. IMPL. BLAKE3
echo REF.txt | .\blake3_reference_impl_c-main\blake3 >> vysledky.txt


cd .\reference_impl
REM RUST: HASOVANIE 10MB SUBORU, POMOCOU REF. IMPL. BLAKE3
cargo run --release .\..\REF.txt >> .\..\vysledky.txt
cd ..

REM PYTHON: HASOVANIE 10MB SUBORU, POMOCOU REF. IMPL. BLAKE3
python .\pure_python_blake3-main\test.py .\REF.txt >> vysledky.txt







REM C: HASOVANIE 20MB SUBORU, POMOCOU REF. IMPL. BLAKE3
echo REF2.txt | .\blake3_reference_impl_c-main\blake3 >> vysledky.txt


cd .\reference_impl
REM RUST: HASOVANIE 20MB SUBORU, POMOCOU REF. IMPL. BLAKE3
cargo run --release .\..\REF2.txt >> .\..\vysledky.txt
cd ..

REM PYTHON: HASOVANIE 20MB SUBORU, POMOCOU REF. IMPL. BLAKE3
python .\pure_python_blake3-main\test.py .\REF2.txt >> vysledky.txt





REM C: HASOVANIE 50MB SUBORU, POMOCOU REF. IMPL. BLAKE3
echo test50.txt | .\blake3_reference_impl_c-main\blake3 >> vysledky.txt


cd .\reference_impl
REM RUST: HASOVANIE 50MB SUBORU, POMOCOU REF. IMPL. BLAKE3
cargo run --release .\..\test50.txt >> .\..\vysledky.txt
cd ..

REM PYTHON: HASOVANIE 50MB SUBORU, POMOCOU REF. IMPL. BLAKE3
python .\pure_python_blake3-main\test.py .\test50.txt >> vysledky.txt