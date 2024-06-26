"""
Module: 'uasyncio.event' on micropython-v1.20.0-rp2-PICO_W
"""

# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
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
