"""
Module: 'ds18x20' on micropython-v1.19.1-rp2
"""

# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def const(*args, **kwargs) -> Any: ...


class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Any: ...

    def write_scratch(self, *args, **kwargs) -> Any: ...

    def read_temp(self, *args, **kwargs) -> Any: ...

    def convert_temp(self, *args, **kwargs) -> Any: ...

    def scan(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
