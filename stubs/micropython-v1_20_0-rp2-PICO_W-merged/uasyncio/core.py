"""
Module: 'uasyncio.core' on micropython-v1.20.0-rp2-PICO_W
"""

# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any


def ticks(*args, **kwargs) -> Any: ...


def run_until_complete(*args, **kwargs) -> Any: ...


def create_task(*args, **kwargs) -> Any: ...


def ticks_diff(*args, **kwargs) -> Any: ...


def run(*args, **kwargs) -> Any: ...


def new_event_loop(*args, **kwargs) -> Any: ...


def current_task(*args, **kwargs) -> Any: ...


def get_event_loop(*args, **kwargs) -> Any: ...


def sleep_ms(*args, **kwargs) -> Any: ...


def ticks_add(*args, **kwargs) -> Any: ...


def sleep(*args, **kwargs) -> Any: ...


class TaskQueue:
    def push(self, *args, **kwargs) -> Any: ...

    def peek(self, *args, **kwargs) -> Any: ...

    def remove(self, *args, **kwargs) -> Any: ...

    def pop(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class Task:
    def __init__(self, *argv, **kwargs) -> None: ...


class CancelledError(Exception): ...
