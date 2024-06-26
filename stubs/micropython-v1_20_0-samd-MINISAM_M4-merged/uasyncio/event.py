"""
Module: 'uasyncio.event' on micropython-v1.20.0-samd-MINISAM_M4
"""

# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'MINISAM_M4', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
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
