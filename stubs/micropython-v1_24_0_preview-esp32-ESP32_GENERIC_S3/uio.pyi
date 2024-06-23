"""
Module: 'uio' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC_S3
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': 'preview.60.gcebc9b0ae', 'arch': 'xtensawin', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'cpu': 'ESP32S3'}
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
