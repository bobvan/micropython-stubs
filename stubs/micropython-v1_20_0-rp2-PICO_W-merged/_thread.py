"""
Multithreading support.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/_thread.html

CPython module: :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.

---
Module: '_thread' on micropython-v1.20.0-rp2-PICO_W
"""

# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any
from _typeshed import Incomplete


def get_ident(*args, **kwargs) -> Any: ...


def start_new_thread(*args, **kwargs) -> Any: ...


def stack_size(*args, **kwargs) -> Any: ...


def exit(*args, **kwargs) -> Any: ...


def allocate_lock(*args, **kwargs) -> Any: ...


class LockType:
    def locked(self, *args, **kwargs) -> Any: ...

    def release(self, *args, **kwargs) -> Any: ...

    def acquire(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
