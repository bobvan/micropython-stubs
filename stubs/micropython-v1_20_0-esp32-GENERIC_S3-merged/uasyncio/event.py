"""
Module: 'uasyncio.event' on micropython-v1.20.0-esp32-GENERIC_S3
"""

# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import Any


class ThreadSafeFlag:
    def set(self, *args, **kwargs) -> Any: ...

    def ioctl(self, *args, **kwargs) -> Any: ...

    def clear(self, *args, **kwargs) -> Any: ...

    wait: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Event:
    def set(self, *args, **kwargs) -> Any: ...

    def is_set(self, *args, **kwargs) -> Any: ...

    def clear(self, *args, **kwargs) -> Any: ...

    wait: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
