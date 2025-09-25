"""
Functions related to the hardware.

MicroPython module: https://docs.micropython.org/en/v1.27.0/library/machine.html

The ``machine`` module contains specific functions related to the hardware
on a particular board. Most functions in this module allow to achieve direct
and unrestricted access to and control of hardware blocks on a system
(like CPU, timers, buses, etc.). Used incorrectly, this can lead to
malfunction, lockups, crashes of your board, and in extreme cases, hardware
damage.
"""

from __future__ import annotations
from _typeshed import Incomplete
from micropython import const as const
from _mpy_shed import _IRQ, AnyReadableBuf, AnyWritableBuf
from typing_extensions import Awaitable, TypeAlias, TypeVar

_path: Incomplete
_PCNT_RANGE: int
IDLE: Incomplete
SLEEP: Incomplete
DEEPSLEEP: Incomplete
PWRON_RESET: Incomplete
HARD_RESET: Incomplete
WDT_RESET: Incomplete
DEEPSLEEP_RESET: Incomplete
SOFT_RESET: Incomplete
WLAN_WAKE: Incomplete
PIN_WAKE: Incomplete
RTC_WAKE: Incomplete
ATTN_0DB: int = ...

class _CounterBase:
    _PCNT: Incomplete
    _INSTANCES: Incomplete
    def __new__(cls, unit_id, *_args, **_kwargs): ...
    _unit_id: Incomplete
    _pcnt: Incomplete
    _overflows: int
    _offset: int
    def __init__(self, unit_id, *args, filter_ns: int = 0, **kwargs) -> None: ...
    def _overflow(self, pcnt) -> None: ...
    def init(self, *args, **kwargs) -> None: ...
    def deinit(self) -> None: ...
    def value(self, value=None): ...

class Counter:
    """
    Returns the singleton Counter object for the the given *id*. Values of *id*
    depend on a particular port and its hardware. Values 0, 1, etc. are commonly
    used to select hardware block #0, #1, etc.

    Additional arguments are passed to the :meth:`init` method described below,
    and will cause the Counter instance to be re-initialised and reset.

    On ESP32, the *id* corresponds to a :ref:`PCNT unit <esp32.PCNT>`.
    """

    RISING: int
    FALLING: int
    UP: Incomplete
    DOWN: Incomplete
    def _configure(self, src, edge=..., direction=...) -> None: ...

class Encoder:
    """
    Returns the singleton Encoder object for the the given *id*. Values of *id*
    depend on a particular port and its hardware. Values 0, 1, etc. are commonly
    used to select hardware block #0, #1, etc.

    Additional arguments are passed to the :meth:`init` method described below,
    and will cause the Encoder instance to be re-initialised and reset.

    On ESP32, the *id* corresponds to a :ref:`PCNT unit <esp32.PCNT>`.
    """

    _phases: Incomplete
    def _configure(self, phase_a, phase_b, phases: int = 1) -> None: ...
    def phases(self): ...

def __getattr__(attr): ...
