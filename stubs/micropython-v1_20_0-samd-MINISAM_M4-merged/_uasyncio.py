"""
Module: '_uasyncio' on micropython-v1.20.0-samd-MINISAM_M4
"""

# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'MINISAM_M4', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any


class TaskQueue:
    def push(self, *args, **kwargs) -> Any: ...

    def peek(self, *args, **kwargs) -> Any: ...

    def remove(self, *args, **kwargs) -> Any: ...

    def pop(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class Task:
    def __init__(self, *argv, **kwargs) -> None: ...
