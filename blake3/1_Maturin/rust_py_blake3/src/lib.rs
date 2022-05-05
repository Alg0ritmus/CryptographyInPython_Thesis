use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn rustypy_blake(_py: Python, data:&[u8]) -> PyResult<[u8;32]>{
    let mut _hasher = blake3::Hasher::new();
     _hasher.update(data);
    let result_from_update =  *_hasher.finalize().as_bytes();
    //Ok("result_from_update");
    return Ok(result_from_update);
       
}
#[pyfunction]
fn rustypy_blake_parallel(_py: Python, data:&[u8]) -> PyResult<[u8;32]>{
    let mut _hasher = blake3::Hasher::new();
     _hasher.update_rayon(data);
    let result_from_update =  *_hasher.finalize().as_bytes();
    //Ok("result_from_update");
    return Ok(result_from_update);
       
}
    


/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn rust_py_blake3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rustypy_blake, m)?)?;
    m.add_function(wrap_pyfunction!(rustypy_blake_parallel, m)?)?;

    Ok(())
}