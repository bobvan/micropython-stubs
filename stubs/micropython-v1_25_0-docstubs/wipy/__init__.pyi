"""
WiPy specific features.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/wipy.html

The ``wipy`` module contains functions to control specific features of the
WiPy, such as the heartbeat LED.
"""

# source version: v1.25.0
# origin module:: repos/micropython/docs/library/wipy.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable

def heartbeat(enable: Optional[Any] = None) -> bool:
    """
    Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and
    returns boolean values (``True`` or ``False``).
    """
    ...
