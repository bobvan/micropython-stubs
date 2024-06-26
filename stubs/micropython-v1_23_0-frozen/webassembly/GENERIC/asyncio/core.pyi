from _asyncio import Task as Task, TaskQueue as TaskQueue
from _typeshed import Incomplete
from collections.abc import Generator

class CancelledError(BaseException): ...
class TimeoutError(Exception): ...

_exc_context: Incomplete

class SingletonGenerator:
    state: Incomplete
    exc: Incomplete
    def __init__(self) -> None: ...
    def __iter__(self): ...
    def __next__(self) -> None: ...

def sleep_ms(t, sgen=...): ...
def sleep(t): ...

asyncio_timer: Incomplete

class ThenableEvent:
    result: Incomplete
    waiting: Incomplete
    def __init__(self, thenable) -> None: ...
    def set(self, value: Incomplete | None = None) -> None: ...
    def remove(self, task) -> None: ...
    def wait(self) -> Generator[None, None, Incomplete]: ...

def _promote_to_task(aw): ...
def _schedule_run_iter(dt) -> None: ...
def _run_iter() -> None: ...
def create_task(coro): ...

cur_task: Incomplete

class Loop:
    _exc_handler: Incomplete
    def create_task(coro): ...
    def close() -> None: ...
    def set_exception_handler(handler) -> None: ...
    def get_exception_handler(): ...
    def default_exception_handler(loop, context) -> None: ...
    def call_exception_handler(context) -> None: ...

def get_event_loop(): ...
def current_task(): ...
def new_event_loop(): ...
