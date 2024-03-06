"""
Module: 'asyncio.__init__' on micropython-v1.23.0-preview-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '176', 'arch': 'armv7emsp', 'ver': '1.23.0-preview-176', 'cpu': 'SAMD51P19A'}
# Stubber: v1.17.3
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

_attrs: dict = {}

def current_task(*args, **kwargs) -> Incomplete: ...
def get_event_loop(*args, **kwargs) -> Incomplete: ...
def create_task(*args, **kwargs) -> Incomplete: ...
def ticks_diff(*args, **kwargs) -> Incomplete: ...
def new_event_loop(*args, **kwargs) -> Incomplete: ...
def ticks(*args, **kwargs) -> Incomplete: ...
def run_until_complete(*args, **kwargs) -> Incomplete: ...
def run(*args, **kwargs) -> Incomplete: ...
def wait_for_ms(*args, **kwargs) -> Incomplete: ...
def sleep_ms(*args, **kwargs) -> Incomplete: ...
def ticks_add(*args, **kwargs) -> Incomplete: ...
def sleep(*args, **kwargs) -> Incomplete: ...

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

open_connection: Generator  ## = <generator>
cur_task: Incomplete  ## <class 'NoneType'> = None
gather: Generator  ## = <generator>

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...

wait_for: Generator  ## = <generator>

class CancelledError(Exception): ...

start_server: Generator  ## = <generator>

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class SingletonGenerator:
    def __init__(self, *argv, **kwargs) -> None: ...

class Loop:
    def get_exception_handler(self, *args, **kwargs) -> Incomplete: ...
    def default_exception_handler(self, *args, **kwargs) -> Incomplete: ...
    def set_exception_handler(self, *args, **kwargs) -> Incomplete: ...
    def run_forever(self, *args, **kwargs) -> Incomplete: ...
    def run_until_complete(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def create_task(self, *args, **kwargs) -> Incomplete: ...
    def call_exception_handler(self, *args, **kwargs) -> Incomplete: ...

    _exc_handler: Incomplete  ## <class 'NoneType'> = None
    def __init__(self, *argv, **kwargs) -> None: ...

class Event:
    def set(self, *args, **kwargs) -> Incomplete: ...
    def is_set(self, *args, **kwargs) -> Incomplete: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class ThreadSafeFlag:
    def set(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class IOQueue:
    def queue_read(self, *args, **kwargs) -> Incomplete: ...
    def wait_io_event(self, *args, **kwargs) -> Incomplete: ...
    def queue_write(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def _enqueue(self, *args, **kwargs) -> Incomplete: ...
    def _dequeue(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class TimeoutError(Exception): ...
