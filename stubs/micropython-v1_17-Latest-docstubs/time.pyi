from typing import Any, Optional, Tuple

class time:
    def __init__(self) -> None: ...

def gmtime(secs: Optional[Any]) -> Tuple: ...
def localtime(secs: Optional[Any]) -> Tuple: ...
def mktime() -> int: ...
def sleep(seconds) -> Any: ...
def sleep_ms(ms) -> None: ...
def sleep_us(us) -> None: ...
def ticks_ms() -> int: ...
def ticks_us() -> Any: ...
def ticks_cpu() -> Any: ...
def ticks_add(ticks, delta) -> Any: ...
def ticks_diff(ticks1, ticks2) -> int: ...
def time_ns() -> int: ...