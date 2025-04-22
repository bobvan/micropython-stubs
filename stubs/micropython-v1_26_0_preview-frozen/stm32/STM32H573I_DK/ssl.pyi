from tls import *
from _typeshed import Incomplete

class SSLContext:
    _context: Incomplete
    def __init__(self, *args) -> None: ...
    @property
    def verify_mode(self): ...
    @verify_mode.setter
    def verify_mode(self, val) -> None: ...
    def load_cert_chain(self, certfile, keyfile) -> None: ...
    def load_verify_locations(self, cafile: Incomplete | None = None, cadata: Incomplete | None = None) -> None: ...
    def wrap_socket(
        self, sock, server_side: bool = False, do_handshake_on_connect: bool = True, server_hostname: Incomplete | None = None
    ): ...

def wrap_socket(
    sock,
    server_side: bool = False,
    key: Incomplete | None = None,
    cert: Incomplete | None = None,
    cert_reqs=...,
    cadata: Incomplete | None = None,
    server_hostname: Incomplete | None = None,
    do_handshake: bool = True,
): ...
