#![allow(unused)]

use std::time::Instant;
use std::env;
mod reference_impl;
use std::fs;
use hex;


fn main(){
    

    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);
    let filename = &args[&args.len()-1];
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    let mut hasher = reference_impl::Hasher::new();
    let now = Instant::now();
    {
        hasher.update(contents.as_bytes());
    }
    let elapsed = now.elapsed();
    let mut hash = [0; 32];
    hasher.finalize(&mut hash);
    println!("RUST: {:?}",filename);
    println!("{:?} \nTime: {:.2?}\n",hex::encode(hash),elapsed);

}
