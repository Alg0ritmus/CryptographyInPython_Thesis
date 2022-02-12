1) vytvor cargo prostredie
    - cargo new 'rustypyblake'

2) Uprav cargo.toml
    [lib]
    name = "rustypyblake"
    crate-type = ["cdylib"]


    [dependencies.pyo3]
    version = "0.15.1"
    features = ["extension-module"]

    [features]
    neon = ["blake3/neon"]

    [dependencies]
    blake3 = { version = "1.0.0", features = ["rayon"] }
    time = "*"
    chrono = "0.4"

3) vytvor lib file -> src/lib.rs

4) build cargo
    - cargo build --release

5) skopiruj target/release/rustypyblake.dll alebo je mozne najst target/release/librustypyblake.dll
6) skopirovany subor vloz do zlozky s py suborom, v ktorom tento (rust-py) modul chceme vyuzivat
7) rustypyblake.dll(alebo librustypyblake.dll ) prepis na -> rustypyblake.pyd (pre windows, pre ine OS check: https://pyo3.rs/latest/building_and_distribution.html)

8) do test_file.py naimportuj tento modul
    - import from rustypyblake



