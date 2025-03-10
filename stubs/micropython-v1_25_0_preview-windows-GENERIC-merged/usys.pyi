"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""

from __future__ import annotations
from _typeshed import Incomplete, Incomplete as Incomplete
from typing import Dict, List, Tuple

modules: dict
version_info: tuple
maxsize: int
version: str
path: list
platform: str
byteorder: str
argv: list
implementation: tuple

def exc_info(*args, **kwargs) -> Incomplete: ...
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

def atexit(func) -> Incomplete:
    """
    Register *func* to be called upon termination.  *func* must be a callable
    that takes no arguments, or ``None`` to disable the call.  The ``atexit``
    function will return the previous value set by this function, which is
    initially ``None``.

    Difference to CPython

       This function is a MicroPython extension intended to provide similar
       functionality to the :mod:`atexit` module in CPython.
    """
    ...

stderr: Incomplete
stdin: Incomplete
stdout: Incomplete
