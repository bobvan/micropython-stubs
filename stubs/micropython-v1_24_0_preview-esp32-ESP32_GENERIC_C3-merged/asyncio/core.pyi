"""
Module: 'asyncio.core' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': 'preview.66.gf60c71d13', 'arch': '', 'ver': '1.24.0-preview-preview.66.gf60c71d13', 'cpu': 'ESP32C3'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

_exc_context: dict = {}

def ticks(*args, **kwargs) -> Incomplete: ...
def create_task(*args, **kwargs) -> Incomplete: ...
def _promote_to_task(*args, **kwargs) -> Incomplete: ...
def ticks_diff(*args, **kwargs) -> Incomplete: ...
def run(*args, **kwargs) -> Incomplete: ...
def run_until_complete(*args, **kwargs) -> Incomplete: ...
def current_task(*args, **kwargs) -> Incomplete: ...
def new_event_loop(*args, **kwargs) -> Incomplete: ...
def get_event_loop(*args, **kwargs) -> Incomplete: ...
def sleep_ms(*args, **kwargs) -> Incomplete: ...
def ticks_add(*args, **kwargs) -> Incomplete: ...
def sleep(*args, **kwargs) -> Incomplete: ...

cur_task: Incomplete  ## <class 'NoneType'> = None
_task_queue: Incomplete  ## <class 'TaskQueue'> = <TaskQueue>

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

class CancelledError(Exception): ...

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...

class TimeoutError(Exception): ...

class IOQueue:
    def queue_read(self, *args, **kwargs) -> Incomplete: ...
    def wait_io_event(self, *args, **kwargs) -> Incomplete: ...
    def queue_write(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def _enqueue(self, *args, **kwargs) -> Incomplete: ...
    def _dequeue(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SingletonGenerator:
    def __init__(self, *argv, **kwargs) -> None: ...

_stopper: Generator  ## = <generator>
_stop_task: Incomplete  ## <class 'NoneType'> = None
_io_queue: Incomplete  ## <class 'IOQueue'> = <IOQueue object at ...>
