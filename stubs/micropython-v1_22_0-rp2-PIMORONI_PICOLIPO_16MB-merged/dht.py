"""
Module: 'dht' on micropython-v1.22.0-rp2-PIMORONI_PICOLIPO_16MB
"""

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO_16MB', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def dht_readinto(*args, **kwargs) -> Incomplete: ...


class DHTBase:
    def measure(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class DHT22:
    def measure(self, *args, **kwargs) -> Incomplete: ...

    def temperature(self, *args, **kwargs) -> Incomplete: ...

    def humidity(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class DHT11:
    def measure(self, *args, **kwargs) -> Incomplete: ...

    def temperature(self, *args, **kwargs) -> Incomplete: ...

    def humidity(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...
