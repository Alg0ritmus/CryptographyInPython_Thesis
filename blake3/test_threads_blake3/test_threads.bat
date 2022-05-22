echo "===RYCHLOSTNY TEST====" > vysledky.txt
REM TEST PARALIZOVATELNEJ RUST IMPL. Blake3 S VYUZITIM 1-8 VLAKIEN CPU
REM SYNTAX: cargo run --release filename threads >> outputfile
cd .\blake3_opt_impl\
cargo build --release 
REM hasovanie 100MB suboru 
cargo run --release ./../test.txt 1 >> ./../vysledky.txt
cargo run --release ./../test.txt 2 >> ./../vysledky.txt
cargo run --release ./../test.txt 3 >> ./../vysledky.txt
cargo run --release ./../test.txt 4 >> ./../vysledky.txt
cargo run --release ./../test.txt 5 >> ./../vysledky.txt
cargo run --release ./../test.txt 6 >> ./../vysledky.txt
cargo run --release ./../test.txt 7 >> ./../vysledky.txt
cargo run --release ./../test.txt 8 >> ./../vysledky.txt
REM hasovanie 200MB suboru 
cargo run --release ./../test2.txt 1 >> ./../vysledky.txt
cargo run --release ./../test2.txt 2 >> ./../vysledky.txt
cargo run --release ./../test2.txt 3 >> ./../vysledky.txt
cargo run --release ./../test2.txt 4 >> ./../vysledky.txt
cargo run --release ./../test2.txt 5 >> ./../vysledky.txt
cargo run --release ./../test2.txt 6 >> ./../vysledky.txt
cargo run --release ./../test2.txt 7 >> ./../vysledky.txt
cargo run --release ./../test2.txt 8 >> ./../vysledky.txt
REM hasovanie 1GB suboru 
cargo run --release ./../test3.txt 1 >> ./../vysledky.txt
cargo run --release ./../test3.txt 2 >> ./../vysledky.txt
cargo run --release ./../test3.txt 3 >> ./../vysledky.txt
cargo run --release ./../test3.txt 4 >> ./../vysledky.txt
cargo run --release ./../test3.txt 5 >> ./../vysledky.txt
cargo run --release ./../test3.txt 6 >> ./../vysledky.txt
cargo run --release ./../test3.txt 7 >> ./../vysledky.txt
cargo run --release ./../test3.txt 8 >> ./../vysledky.txt
cd ..

REM TEST PARALIZ. RUST_PY_BLAKE3 DYNAMICKEJ KNIZNICE (PYD) S VYUZITIM 1-8 VLAKIEN CPU
REM SYNTAX: python filename threads >> outputfile
REM hasovanie 100MB suboru 
python .\test.py test.txt 1 >> vysledky.txt 
python .\test.py test.txt 2 >> vysledky.txt 
python .\test.py test.txt 3 >> vysledky.txt 
python .\test.py test.txt 4 >> vysledky.txt 
python .\test.py test.txt 5 >> vysledky.txt 
python .\test.py test.txt 6 >> vysledky.txt 
python .\test.py test.txt 7 >> vysledky.txt 
python .\test.py test.txt 8 >> vysledky.txt 
REM hasovanie 200MB suboru 
python .\test.py test2.txt 1 >> vysledky.txt 
python .\test.py test2.txt 2 >> vysledky.txt 
python .\test.py test2.txt 3 >> vysledky.txt 
python .\test.py test2.txt 4 >> vysledky.txt 
python .\test.py test2.txt 5 >> vysledky.txt 
python .\test.py test2.txt 6 >> vysledky.txt 
python .\test.py test2.txt 7 >> vysledky.txt 
python .\test.py test2.txt 8 >> vysledky.txt 
REM hasovanie 1GB suboru 
python .\test.py test3.txt 1 >> vysledky.txt 
python .\test.py test3.txt 2 >> vysledky.txt 
python .\test.py test3.txt 3 >> vysledky.txt 
python .\test.py test3.txt 4 >> vysledky.txt 
python .\test.py test3.txt 5 >> vysledky.txt 
python .\test.py test3.txt 6 >> vysledky.txt 
python .\test.py test3.txt 7 >> vysledky.txt 
python .\test.py test3.txt 8 >> vysledky.txt 

