1) create Cargo crate
    - cargo new 'RustBlake'

2) install b3sum
    - cargo instal b3sum

3) pridaj blake3 do Cargo.toml + daksie dependencies/feat.
    [features]
    neon = ["blake3/neon"]

    [dependencies]
    blake3 = { version = "1.0.0", features = ["rayon"] }
    time = "*"
    chrono = "0.4"

4) re-run cargo build
    - cargo build

5) vloz kod do  src/main.rs

6) cargo run


!!!!!!!!!!!!!!!!!!!!!!!!!!!!
predosle spustenie kodu je v dev mode -> developersky debuggovaci mod
pre vyuzitie plnej rychlosti kodu, pouzi optimized mode

8) cargo run --release