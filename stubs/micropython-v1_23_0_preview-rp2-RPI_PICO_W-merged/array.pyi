"""
Efficient arrays of numeric data.

MicroPython module: https://docs.micropython.org/en/v1.23.0.preview/library/array.html

CPython module: :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).

---
Module: 'array' on micropython-v1.23.0-preview-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.23.0-preview', 'build': 'preview.58.gc3ca3612d', 'ver': '1.23.0-preview-preview.58.gc3ca3612d', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, List, Optional

class array(List):
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def extend(self, iterable) -> Incomplete:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...
    def append(self, val) -> Incomplete:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
