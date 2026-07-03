# Micropython v1.29.0-preview frozen stubs
"""
Basic "operating system" services.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/os.html

CPython module: :mod:`python:os` https://docs.python.org/3/library/os.html .

The ``os`` module contains functions for filesystem access and mounting,
terminal redirection and duplication, and the ``uname`` and ``urandom``
functions.
"""

from __future__ import annotations
from uos import *
from _typeshed import Incomplete
from typing import NamedTuple
from _mpy_shed import uname_result
from typing_extensions import Awaitable, TypeAlias, TypeVar

class stat_result(NamedTuple):
    st_mode: Incomplete
    st_ino: Incomplete
    st_dev: Incomplete
    st_nlink: Incomplete
    st_uid: Incomplete
    st_gid: Incomplete
    st_size: Incomplete
    st_atime: Incomplete
    st_mtime: Incomplete
    st_ctime: Incomplete

__os_stat = stat

def stat(path) -> Incomplete:
    """
    Get the status of a file or directory.
    """
    ...
