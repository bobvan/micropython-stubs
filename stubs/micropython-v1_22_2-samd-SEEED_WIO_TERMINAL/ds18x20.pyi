"""
Module: 'ds18x20' on micropython-v1.22.2-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

def const(*args, **kwargs) -> Incomplete: ...

class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Incomplete: ...
    def read_temp(self, *args, **kwargs) -> Incomplete: ...
    def write_scratch(self, *args, **kwargs) -> Incomplete: ...
    def convert_temp(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
