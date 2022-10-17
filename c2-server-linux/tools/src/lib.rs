#![allow(unused)]

use std::fs;
use std::path::Path;
use walkdir::WalkDir;
use rsa::{RsaPublicKey, pkcs8::DecodePublicKey};

const PUB_KEY_PEM: &str = "-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA40ZZiWWyr5n3b4dhCo8I
hqMwxai6qG/wXoctjhbjwoxXBtR3CNM8TVhKqZjJTcCBFOEqKLDDTIx7FAm4jCTk
BXTNqvuWXDraZd2M0BIwePh0bShLzQE+ZIZ7eIbwhuHX9lUytQBPQtqHnQfHNUO5
JTHJ7CEzvnp4wIzchBhwfOCSM7202HqXiMq4mZrgnjxX+5tq3N7u4SF/yVd94L1f
6qVWvHMWOxIAFIbHIksNp+XHiF5rbfSfxik7Wy8IAcxFRz76wf4jNSJBeMZEPQb6
Pm32RZybMPivc1LQgI5KoLqQf0d5RRPnSjajMPY8Hed/j7qviqD+4akzalFwo36i
j3PnZH3cQqEfGt9zMqO+o9idJYEfEuLg+Gcsj9Mas+faPGCCQuz6OjtO1DTFMag4
+norgLoTMDEXxBrl6jonTJLZxdmiXULwCkAx+vfRm9HL7MPTFHjqE1w0KA98k9o4
oNZ45AHE0ZmEWxGIdHl20jfA9xFNgOScqni+tDRpqMq7F772zfd9PAML4CZHru9T
QHiNvtXu5GjglKIppX/VOHu61f7KYnZYZN/AL+YnpYjXz8SU+PRhr5h/1fIG858g
TwOAIcXA6EFpBlLw1T6FMJXJ71AP/iykzMqp8cAJHtsLzKYyTQIpRrfKjFqHde3A
Oyn5xrw9cy8p7S+eDOUUQykCAwEAAQ==
-----END PUBLIC KEY-----";

pub fn encrypt_file() {
    println!("encrypt_file");
}

pub fn encrypt_dir() {
    println!("encrypt_dir");

    /*
        Navigate through directory
        - Check extension
        - call encrypt file on only *.decrypted
          - change file extension to *.encrypted
     */
     let paths = fs::read_dir("./TestDirectories").unwrap();

     for path in paths {
         println!("Encrypting the following: {}", path.unwrap().path().display())
     }


}
