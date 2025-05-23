"""
Collection and container types.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/collections.html

CPython module: :mod:`python:collections` https://docs.python.org/3/library/collections.html .

This module implements advanced collection and container types to
hold/accumulate various objects.

---
Module: 'collections' on micropython-v1.21.0-esp32-ESP32_GENERIC_S3
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.21.0', 'cpu': 'ESP32S3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from stdlib.collections import OrderedDict as stdlib_OrderedDict, deque as stdlib_deque, namedtuple as stdlib_namedtuple
from typing import Any, Optional

def namedtuple(name, fields) -> stdlib_namedtuple:
    """
    This is factory function to create a new namedtuple type with a specific
    name and set of fields. A namedtuple is a subclass of tuple which allows
    to access its fields not just by numeric index, but also with an attribute
    access syntax using symbolic field names. Fields is a sequence of strings
    specifying field names. For compatibility with CPython it can also be a
    a string with space-separated field named (but this is less efficient).
    Example of use::

        from collections import namedtuple

        MyTuple = namedtuple("MyTuple", ("id", "name"))
        t1 = MyTuple(1, "foo")
        t2 = MyTuple(2, "bar")
        print(t1.name)
        assert t2.name == t2[1]
    """
    ...

class OrderedDict(stdlib_OrderedDict):
    """
    ``dict`` type subclass which remembers and preserves the order of keys
    added. When ordered dict is iterated over, keys/items are returned in
    the order they were added::

        from collections import OrderedDict

        # To make benefit of ordered keys, OrderedDict should be initialized
        # from sequence of (key, value) pairs.
        d = OrderedDict([("z", 1), ("a", 2)])
        # More items can be added as usual
        d["w"] = 5
        d["b"] = 3
        for k, v in d.items():
            print(k, v)

    Output::

        z 1
        a 2
        w 5
        b 3
    """

    def popitem(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def values(self, *args, **kwargs) -> Incomplete: ...
    def setdefault(self, *args, **kwargs) -> Incomplete: ...
    def update(self, *args, **kwargs) -> Incomplete: ...
    def copy(self, *args, **kwargs) -> Incomplete: ...
    def clear(self, *args, **kwargs) -> Incomplete: ...
    def keys(self, *args, **kwargs) -> Incomplete: ...
    def get(self, *args, **kwargs) -> Incomplete: ...
    def items(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class deque(stdlib_deque):
    """
    Deques (double-ended queues) are a list-like container that support O(1)
    appends and pops from either side of the deque.  New deques are created
    using the following arguments:

        - *iterable* is an iterable used to populate the deque when it is
          created.  It can be an empty tuple or list to create a deque that
          is initially empty.

        - *maxlen* must be specified and the deque will be bounded to this
          maximum length.  Once the deque is full, any new items added will
          discard items from the opposite end.

        - The optional *flags* can be 1 to check for overflow when adding items.

    Deque objects support `bool`, `len`, iteration and subscript load and store.
    They also have the following methods:
    """

    def popleft(self) -> Incomplete:
        """
        Remove and return an item from the left side of the deque.
        Raises ``IndexError`` if no items are present.
        """
        ...

    def append(self, x) -> Incomplete:
        """
        Add *x* to the right side of the deque.
        Raises ``IndexError`` if overflow checking is enabled and there is
        no more room in the queue.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None: ...
