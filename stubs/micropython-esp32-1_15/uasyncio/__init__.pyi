
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class CancelledError: ...
class Event:
    def clear() -> None: ...
    def is_set() -> None: ...
    def set() -> None: ...
class IOQueue:
    def _dequeue() -> None: ...
    def _enqueue() -> None: ...
    def queue_read() -> None: ...
    def queue_write() -> None: ...
    def remove() -> None: ...
    def wait_io_event() -> None: ...
class Lock:
    def locked() -> None: ...
    def release() -> None: ...
class Loop:
    def call_exception_handler() -> None: ...
    def close() -> None: ...
    def create_task() -> None: ...
    def default_exception_handler() -> None: ...
    def get_exception_handler() -> None: ...
    def run_forever() -> None: ...
    def run_until_complete() -> None: ...
    def set_exception_handler() -> None: ...
    def stop() -> None: ...
class SingletonGenerator: ...
class StreamReader:
    def close() -> None: ...
    def get_extra_info() -> None: ...
    def write() -> None: ...
class StreamWriter:
    def close() -> None: ...
    def get_extra_info() -> None: ...
    def write() -> None: ...
class Task: ...
class TaskQueue:
    def peek() -> None: ...
    def pop_head() -> None: ...
    def push_head() -> None: ...
    def push_sorted() -> None: ...
    def remove() -> None: ...
class ThreadSafeFlag:
    def ioctl() -> None: ...
    def set() -> None: ...
class TimeoutError: ...
def create_task() -> None: ...
def current_task() -> None: ...
def get_event_loop() -> None: ...
def new_event_loop() -> None: ...
def run() -> None: ...
def run_until_complete() -> None: ...
def sleep() -> None: ...
def sleep_ms() -> None: ...
def ticks() -> None: ...
def ticks_add() -> None: ...
def ticks_diff() -> None: ...
def wait_for_ms() -> None: ...
