"""
Module: 'ntptime' on micropython-v1.20.0-rp2-PICO_W
"""

# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any

timeout = 1  # type: int
host = "pool.ntp.org"  # type: str


def settime(*args, **kwargs) -> Any: ...


def time(*args, **kwargs) -> Any: ...
