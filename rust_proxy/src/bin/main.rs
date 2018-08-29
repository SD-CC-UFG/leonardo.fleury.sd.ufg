extern crate ruschat_server;
extern crate url;
extern crate http_muncher;

use std::str;
use ruschatServer::ThreadPool;
use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;
use std::net::Shutdown;
use http_muncher::{Parser, ParserHandler};

struct HttpHandler{}

impl ParserHandler for HttpHandler{
    fn on_url(&mut self, parser: &mut Parser, url: &[u8]) -> bool {
        println!("url: {:?}", str::from_utf8(url).unwrap());
        true
    }

    fn on_body(&mut self, parser: &mut Parser, body: &[u8]) -> bool {
        println!("body: {:?}", str::from_utf8(body).unwrap());
        true
    }

    fn on_header_field(&mut self, parser: &mut Parser, header: &[u8]) -> bool {
       println!("header: {}: ", str::from_utf8(header).unwrap());
       true
   }

   fn on_header_value(&mut self, parser: &mut Parser, value: &[u8]) -> bool {
       println!("\t {:?}", str::from_utf8(value).unwrap());
       true
   }
}

fn handle_client(mut stream: TcpStream) {
    loop {
        let mut parser = Parser::request();
        let mut buf = [0; 1024];

        stream.read(&mut buf).unwrap();

        let message = String::from_utf8_lossy(&buf[..]);

        parser.parse(&mut HttpHandler {}, message.as_bytes());

        println!("{:?}", parser);
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
    let pool = ThreadPool::new(32);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_client(stream);
        });
    }

    println!("Desligando!");
}
