"""
Module: 'io' on micropython-v1.22.2-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def open(*args, **kwargs) -> Incomplete: ...

class IOBase:
    def __init__(self, *argv, **kwargs) -> None: ...

class StringIO:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def getvalue(self, *args, **kwargs) -> Incomplete: ...
    def seek(self, *args, **kwargs) -> Incomplete: ...
    def tell(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class BytesIO:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def getvalue(self, *args, **kwargs) -> Incomplete: ...
    def seek(self, *args, **kwargs) -> Incomplete: ...
    def tell(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
