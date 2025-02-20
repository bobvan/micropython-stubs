"""
System error codes.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/errno.html

CPython module: :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.

---
Module: 'uerrno' on micropython-v1.21.0-webassembly-GENERIC
"""

from __future__ import annotations

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'webassembly', 'board': 'GENERIC', 'cpu': 'Emscripten', 'mpy': '', 'arch': ''}
# Stubber: v1.15.0
from typing import Dict, Any
from _typeshed import Incomplete

ENOBUFS = 105  # type: int
ENODEV = 19  # type: int
ENOENT = 2  # type: int
EISDIR = 21  # type: int
EIO = 5  # type: int
EINVAL = 22  # type: int
EPERM = 1  # type: int
ETIMEDOUT = 110  # type: int
ENOMEM = 12  # type: int
EOPNOTSUPP = 95  # type: int
ENOTCONN = 107  # type: int
errorcode = {}  # type: dict
EAGAIN = 11  # type: int
EALREADY = 114  # type: int
EBADF = 9  # type: int
EADDRINUSE = 98  # type: int
EACCES = 13  # type: int
EINPROGRESS = 115  # type: int
EEXIST = 17  # type: int
EHOSTUNREACH = 113  # type: int
ECONNABORTED = 103  # type: int
ECONNRESET = 104  # type: int
ECONNREFUSED = 111  # type: int
