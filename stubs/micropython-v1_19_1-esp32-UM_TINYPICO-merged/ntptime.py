"""
Module: 'ntptime' on micropython-v1.19.1-esp32
"""

# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


def time(*args, **kwargs) -> Any: ...


def settime(*args, **kwargs) -> Any: ...


NTP_DELTA = 3155673600  # type: int
host = "pool.ntp.org"  # type: str
