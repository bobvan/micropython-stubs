"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .

---
Module: 'sys' on micropython-v1.21.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.21.0', 'cpu': 'ESP32'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Dict, List, Tuple

platform: str = "esp32"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.21.0 on 2023-10-05"
ps1: str = ">>> "
ps2: str = "... "
byteorder: str = "little"
modules: dict = {}
argv: list = []
implementation: tuple = ()
maxsize: int = 2147483647

def print_exception(
    exc,
    file=stdout,
) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).

    Difference to CPython

       This is simplified version of a function which appears in the
       ``traceback`` module in CPython. Unlike ``traceback.print_exception()``,
       this function takes just exception value instead of exception type,
       exception value, and traceback object; *file* argument should be
       positional; further arguments are not supported. CPython-compatible
       ``traceback`` module can be found in `micropython-lib`.
    """
    ...

def exit(
    retval=0,
) -> Incomplete:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raises a `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.

    On embedded ports (i.e. all ports but Windows and Unix), an unhandled
    `SystemExit` currently causes a :ref:`soft_reset` of MicroPython.
    """
    ...

stderr: Incomplete  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Incomplete  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Incomplete  ## <class 'FileIO'> = <io.FileIO 0>
