from ubinascii import *
from _typeshed import Incomplete

def unhexlify(data): ...

b2a_hex = hexlify
a2b_hex = unhexlify
PAD: str
table_a2b_base64: Incomplete

def _transform(n): ...
def a2b_base64(ascii):
    """Decode a line of base64 data."""

table_b2a_base64: str

def b2a_base64(bin, newline: bool = True):
    """Base64-code line of data."""
