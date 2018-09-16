extern crate http_muncher;

use self::http_muncher::{Parser, ParserHandler};
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;
use std::str;

#[derive(Default, Debug)]
pub struct HttpHandler {
    url: Option<String>,
    headers: Rc<RefCell<HashMap<String, String>>>,
    _current_key: Option<String>,
    body: String,
}

impl ParserHandler for HttpHandler {
    fn on_url(&mut self, parser: &mut Parser, value: &[u8]) -> bool {
        self.url = Some(str::from_utf8(value).unwrap().to_string());
        true
    }

    fn on_status(&mut self, parser: &mut Parser, value: &[u8]) -> bool {
        println!("status: {}: ", str::from_utf8(value).unwrap());
        true
    }

    fn on_header_field(&mut self, parser: &mut Parser, header: &[u8]) -> bool {
        self._current_key = Some(str::from_utf8(header).unwrap().to_string());
        true
    }

    fn on_header_value(&mut self, parser: &mut Parser, value: &[u8]) -> bool {
        self.headers.borrow_mut().insert(
            self._current_key.clone().unwrap(),
            str::from_utf8(value).unwrap().to_string(),
        );
        true
    }

    fn on_headers_complete(&mut self, parser: &mut Parser) -> bool {
        self._current_key = None;
        true
    }

    fn on_body(&mut self, parser: &mut Parser, value: &[u8]) -> bool {
        self.body = String::from_utf8_lossy(value).to_string();
        true
    }
}
