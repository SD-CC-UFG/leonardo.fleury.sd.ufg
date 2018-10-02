use std::net::TcpListener;
use std::net::TcpStream;
use std::net::Ipv4Addr;

use std::collections::HashMap;

use name_server::entry;

fn handle_client(stream: TcpStream, servers_map: HashMap<String, String>) {
    
}

fn main () {
    let listener = TcpListener::bind("127.0.0.1:6000").unwrap();

    let mut servers = HashMap<String, String>::new();

    for stream in listener.incoming() {
        match stream {
            Ok(s) => {
                handle_client(s, servers);
            }
            Err(e) => {
                println!("encountered IO error: {}", e);
            }
        }
    }
}