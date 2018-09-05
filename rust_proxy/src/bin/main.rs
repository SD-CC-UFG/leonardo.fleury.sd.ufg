extern crate rust_proxy;

use std::str;
use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;

use rust_proxy::threadpool::ThreadPool;

fn handle_client(mut stream: TcpStream) {
    let mut buf = [0; 1024];

    stream.read(&mut buf).unwrap();
        
    let req: Vec<&str> = str::from_utf8(& buf).unwrap().split("\r\n").collect();

    println!("{:#?}", req);
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    let pool = ThreadPool::new(32);

    println!("Servidor iniciado em {}", listener.local_addr().unwrap());

    for stream in listener.incoming() {
        match stream {
            Ok(s) => {
                pool.execute(|| {
                    handle_client(s);
                });
            },
            Err(e) => panic!("encountered IO error: {}", e),
        }
    }

    println!("Desligando!");
}
