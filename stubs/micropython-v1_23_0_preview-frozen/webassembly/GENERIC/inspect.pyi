from _typeshed import Incomplete
from collections.abc import Generator

def getmembers(obj, pred: Incomplete | None = None): ...
def isfunction(obj): ...
def isgeneratorfunction(obj) -> Generator[None, None, Incomplete]: ...
def isgenerator(obj) -> Generator[None, None, Incomplete]: ...

class _Class:
    def meth() -> None: ...

_Instance: Incomplete

def ismethod(obj): ...
def isclass(obj): ...
def ismodule(obj): ...
def getargspec(func) -> None: ...
def getmodule(obj, _filename: Incomplete | None = None) -> None: ...
def getmro(cls): ...
def getsourcefile(obj) -> None: ...
def getfile(obj): ...
def getsource(obj): ...
def currentframe() -> None: ...
def getframeinfo(frame, context: int = 1): ...