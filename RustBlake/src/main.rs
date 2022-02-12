use std::fs::File;
use std::io::prelude::*;
use std::time::Instant;

fn main(){
    let mut file = File::open("-/../../../test.txt").expect("err"); // 200MB file that I want to hash
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("err2");
    
    let mut _hasher = blake3::Hasher::new();
    

    let binary_file = contents.as_bytes();

    let now = Instant::now();

    {

        _hasher.update_rayon(binary_file);  



         
     let result_from_update =  _hasher.finalize().to_hex();
    println!("result from update {}",result_from_update);
    }

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}