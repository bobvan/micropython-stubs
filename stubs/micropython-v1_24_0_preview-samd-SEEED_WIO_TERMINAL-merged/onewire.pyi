"""
Module: 'onewire' on micropython-v1.24.0-preview-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '62', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-62', 'cpu': 'SAMD51P19A'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

class OneWireError(Exception): ...

class OneWire:
    SKIP_ROM: int = 204
    SEARCH_ROM: int = 240
    MATCH_ROM: int = 85
    def select_rom(self, *args, **kwargs) -> Incomplete: ...
    def writebit(self, *args, **kwargs) -> Incomplete: ...
    def writebyte(self, *args, **kwargs) -> Incomplete: ...
    def _search_rom(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def crc8(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def reset(self, *args, **kwargs) -> Incomplete: ...
    def readbit(self, *args, **kwargs) -> Incomplete: ...
    def readbyte(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
