"""
Module: 'dht' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


def dht_readinto(*args, **kwargs) -> Any:
    ...


class DHTBase:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...


class DHT11:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...


class DHT22:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...
