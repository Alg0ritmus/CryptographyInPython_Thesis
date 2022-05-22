// Autor: Patrik Zeleňák
// Verzia: 0.1
// Poznámka: Následujúci kód bol vytvorený
// v rámci bakalárskej práce - Kryptografia v Pythone

// import balika PyO3 a rayon -> paralelizmus
use pyo3::prelude::*;
use rayon::prelude::*;


#[pyfunction]
fn rustypy_blake(_py: Python, data:&[u8]) -> PyResult<[u8;32]>{
    let mut _hasher = blake3::Hasher::new();
     _hasher.update(data);
    let result_from_update =  *_hasher.finalize().as_bytes();
    return Ok(result_from_update);
       
}
#[pyfunction]
fn rustypy_blake_parallel(_py: Python, data:&[u8], threads_num: usize) -> PyResult<[u8;32]>{
    rayon::ThreadPoolBuilder::new().num_threads(threads_num).build_global().unwrap(); // pridanie parametrizovatelneho vyuzitia vlakien
    let mut _hasher = blake3::Hasher::new();
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