import os
from _typeshed import Incomplete

class LS:
    def __repr__(self) -> str: ...
    def __call__(self, path: str = ".") -> None: ...

class PWD:
    def __repr__(self) -> str: ...
    def __call__(self): ...

class CLEAR:
    def __repr__(self) -> str: ...
    def __call__(self): ...

def head(f, n: int = 10) -> None: ...
def cat(f) -> None: ...
def cp(s, t) -> None: ...
def newfile(path) -> None: ...
def rm(d, recursive: bool = False) -> None: ...

class Man:
    def __repr__(self) -> str: ...

man: Incomplete
pwd: Incomplete
ls: Incomplete
clear: Incomplete
cd = os.chdir
mkdir = os.mkdir
mv = os.rename
rmdir = os.rmdir