# Copyright (c) 2019, Digi International, Inc.

import uio
from .uio import FileIO, _IOBase

from typing import Any, Dict, List, Optional, Tuple

argv: List[str] = ...
byteorder: str = ...
implementation: Tuple[str, Tuple[int, int, int], int] = ...
maxsize: int = ...
modules: Dict[str, Any] = ...  # technically [str, Module]
path: List[str] = ...
platform: str = ...
stderr: FileIO = ...
stdin: FileIO = ...
stdout: FileIO = ...
version: str = ...
version_info: Tuple[int, int, int] = ...

def exit(arg: Optional[object] = None, /) -> None:
    """
    Raise a ``SystemExit`` exception, with the given argument if specified.

    Note that calling ``sys.exit()`` while at the MicroPython REPL
    (``>>>`` prompt) has no effect.
    """

def print_exception(exc: BaseException, file: _IOBase = stdout, /) -> None:
    """
    Print the given exception and its traceback to a file-like object
    (default is ``sys.stdout``).

    This is a simplified version of CPython's ``traceback.print_exception()``
    function.
    """