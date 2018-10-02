use std::net::Ipv4Addr;

pub struct Entry {
    name: String,
    address: Ipv4Addr,
    port: u16 
}

impl Entry {
    pub fn new(&mut self, name: String, address: Ipv4Addr, port: u16) -> Entry {
        Entry{
            name,
            address,
            port
        }
    }
}