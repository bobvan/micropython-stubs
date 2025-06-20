from _typeshed import Incomplete
from micropython import const as const

CRITICAL: int
ERROR: int
WARNING: int
INFO: int
DEBUG: int
NOTSET: int
_DEFAULT_LEVEL = WARNING
_level_dict: Incomplete
_loggers: Incomplete
_stream: Incomplete
_default_fmt: str
_default_datefmt: str

class LogRecord:
    name: Incomplete
    levelno: Incomplete
    levelname: Incomplete
    message: Incomplete
    ct: Incomplete
    msecs: Incomplete
    asctime: Incomplete
    def set(self, name, level, message) -> None: ...

class Handler:
    level: Incomplete
    formatter: Incomplete
    def __init__(self, level=...) -> None: ...
    def close(self) -> None: ...
    def setLevel(self, level) -> None: ...
    def setFormatter(self, formatter) -> None: ...
    def format(self, record): ...

class StreamHandler(Handler):
    stream: Incomplete
    terminator: str
    def __init__(self, stream: Incomplete | None = None) -> None: ...
    def close(self) -> None: ...
    def emit(self, record) -> None: ...

class FileHandler(StreamHandler):
    def __init__(self, filename, mode: str = "a", encoding: str = "UTF-8") -> None: ...
    def close(self) -> None: ...

class Formatter:
    fmt: Incomplete
    datefmt: Incomplete
    def __init__(self, fmt: Incomplete | None = None, datefmt: Incomplete | None = None) -> None: ...
    def usesTime(self): ...
    def formatTime(self, datefmt, record): ...
    def format(self, record): ...

class Logger:
    name: Incomplete
    level: Incomplete
    handlers: Incomplete
    record: Incomplete
    def __init__(self, name, level=...) -> None: ...
    def setLevel(self, level) -> None: ...
    def isEnabledFor(self, level): ...
    def getEffectiveLevel(self): ...
    def log(self, level, msg, *args) -> None: ...
    def debug(self, msg, *args) -> None: ...
    def info(self, msg, *args) -> None: ...
    def warning(self, msg, *args) -> None: ...
    def error(self, msg, *args) -> None: ...
    def critical(self, msg, *args) -> None: ...
    def exception(self, msg, *args, exc_info: bool = True) -> None: ...
    def addHandler(self, handler) -> None: ...
    def hasHandlers(self): ...

def getLogger(name: Incomplete | None = None): ...
def log(level, msg, *args) -> None: ...
def debug(msg, *args) -> None: ...
def info(msg, *args) -> None: ...
def warning(msg, *args) -> None: ...
def error(msg, *args) -> None: ...
def critical(msg, *args) -> None: ...
def exception(msg, *args, exc_info: bool = True) -> None: ...
def shutdown() -> None: ...
def addLevelName(level, name) -> None: ...
def basicConfig(
    filename: Incomplete | None = None,
    filemode: str = "a",
    format: Incomplete | None = None,
    datefmt: Incomplete | None = None,
    level=...,
    stream: Incomplete | None = None,
    encoding: str = "UTF-8",
    force: bool = False,
) -> None: ...
