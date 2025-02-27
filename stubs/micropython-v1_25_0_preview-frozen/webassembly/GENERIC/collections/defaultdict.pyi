"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.
"""

from __future__ import annotations
from _typeshed import Incomplete
from stdlib.collections import OrderedDict as stdlib_OrderedDict, deque as stdlib_deque, namedtuple as stdlib_namedtuple

class defaultdict:
    d: Incomplete
    @staticmethod
    def __new__(cls, default_factory: Incomplete | None = None, **kwargs): ...
    default_factory: Incomplete
    def __init__(self, default_factory: Incomplete | None = None, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, v) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __missing__(self, key): ...
