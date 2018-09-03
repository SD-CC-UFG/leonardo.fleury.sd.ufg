extern crate ruschat_server;

use std::str;
use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;

use ruschat_server::ThreadPool;

fn handle_client(mut stream: TcpStream) {
    loop {
        let mut buf = [0; 1024];

        stream.read(&mut buf).unwrap();
        
        let req = str::from_utf8(& buf);

        println!("{:#?}", req);
    }
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
