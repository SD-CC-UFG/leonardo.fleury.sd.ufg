extern crate rust_proxy;

#[macro_use]
extern crate log;
extern crate env_logger;

extern crate http_muncher;

use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;

use http_muncher::Parser;

use rust_proxy::http_parser::HttpHandler;
use rust_proxy::threadpool::ThreadPool;

fn handle_client(mut stream: TcpStream) {
    let mut buf = [0; 1024];
    let mut parser = Parser::request();
    let mut handler = HttpHandler::default();

    stream.read(&mut buf).unwrap();
    parser.parse(&mut handler, &buf);

    debug!("{:#?}", handler);
}

fn main() {
    env_logger::init();

    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    let pool = ThreadPool::new(32);

    info!("Servidor iniciado em {}", listener.local_addr().unwrap());

    for stream in listener.incoming() {
        match stream {
            Ok(s) => {
                pool.execute(|| {
                    handle_client(s);
                });
            }
            Err(e) => {
                error!("encountered IO error: {}", e);
            }
        }
    }

    info!("Desligando!");
}
