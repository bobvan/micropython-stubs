# Replace built-in os module.
"""
Basic "operating system" services.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/os.html

CPython module: :mod:`python:os` https://docs.python.org/3/library/os.html .

The ``os`` module contains functions for filesystem access and mounting,
terminal redirection and duplication, and the ``uname`` and ``urandom``
functions.
"""
from __future__ import annotations
from uos import *
from _typeshed import Incomplete
from stdlib.os import *

# Provide optional dependencies (which may be installed separately).
try:
    from . import path
except ImportError:
    pass
