"""
Module: 'io' on micropython-v1.21.0-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': '', 'arch': '', 'ver': '1.21.0', 'cpu': 'ESP32C3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def open(*args, **kwargs) -> Incomplete: ...

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

class IOBase:
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

class BufferedWriter:
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
