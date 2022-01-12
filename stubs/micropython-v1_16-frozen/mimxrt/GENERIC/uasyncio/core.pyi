from .task import Task as Task, TaskQueue as TaskQueue
from typing import Any

class CancelledError(BaseException): ...
class TimeoutError(Exception): ...

_exc_context: Any

class SingletonGenerator:
    state: Any
    exc: Any
    def __init__(self) -> None: ...
    def __iter__(self): ...
    def __next__(self) -> None: ...

def sleep_ms(t, sgen=...): ...
def sleep(t): ...

class IOQueue:
    poller: Any
    map: Any
    def __init__(self) -> None: ...
    def _enqueue(self, s, idx) -> None: ...
    def _dequeue(self, s) -> None: ...
    def queue_read(self, s) -> None: ...
    def queue_write(self, s) -> None: ...
    def remove(self, task) -> None: ...
    def wait_io_event(self, dt) -> None: ...

def _promote_to_task(aw): ...
def create_task(coro): ...
def run_until_complete(main_task: Any | None = ...): ...
def run(coro): ...
async def _stopper() -> None: ...

_stop_task: Any

class Loop:
    _exc_handler: Any
    def create_task(coro): ...
    def run_forever() -> None: ...
    def run_until_complete(aw): ...
    def stop() -> None: ...
    def close() -> None: ...
    def set_exception_handler(handler) -> None: ...
    def get_exception_handler(): ...
    def default_exception_handler(loop, context) -> None: ...
    def call_exception_handler(context) -> None: ...

def get_event_loop(runq_len: int = ..., waitq_len: int = ...): ...
def current_task(): ...
def new_event_loop(): ...