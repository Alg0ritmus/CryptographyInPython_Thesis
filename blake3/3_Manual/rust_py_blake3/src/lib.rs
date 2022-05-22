// Autor: Patrik Zeleňák
// Verzia: 0.1
// Poznámka: Následujúci kód bol vytvorený
// v rámci bakalárskej práce - Kryptografia v Pythone

// import balika PyO3
use pyo3::prelude::*;

// Mapovanie Rust modulu Blake3 do jazyka Python s vyuzitim PyO3
// Definovanie funkcii, kt. bude mozno volat z jazyka Python musi
// zacinat makrom #[pyfunction]
#[pyfunction]
fn rustypy_blake(_py: Python, data:&[u8]) -> PyResult<[u8;32]>{
    let mut _hasher = blake3::Hasher::new();
    // hasovanie dat vyuzitim 1 vlakna
     _hasher.update(data);
    let result_from_update =  *_hasher.finalize().as_bytes();
    return Ok(result_from_update);
       
}
#[pyfunction]
fn rustypy_blake_parallel(_py: Python, data:&[u8]) -> PyResult<[u8;32]>{
    let mut _hasher = blake3::Hasher::new();
    // paralelne hasovanie dat vyuzitim vsetkych dostupnych vlakien CPU
     _hasher.update_rayon(data);
    let result_from_update =  *_hasher.finalize().as_bytes();
    return Ok(result_from_update);
       
}
    


// Zviazanie vytvorenych funkcii. Nutne pre spravne volanie funkcii
// definovanych vyssie. Funkcia nizsie musi mat rovnake meno ako sme 
// zadavali v subore Cargo.toml (vid Bc. praca).
#[pymodule]
fn rust_py_blake3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rustypy_blake, m)?)?;
    m.add_function(wrap_pyfunction!(rustypy_blake_parallel, m)?)?;
    Ok(())
}