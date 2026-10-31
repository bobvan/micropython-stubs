"""
Functionality specific to NXP i.MXRT.

MicroPython module: https://docs.micropython.org/en/preview.0/library/mimxrt.html

The ``mimxrt`` module contains functions and classes specific to the NXP i.MXRT
family of microcontrollers.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/mimxrt.rst
from __future__ import annotations

from _typeshed import Incomplete
from mimxrt.Flash import Flash
from typing_extensions import Awaitable, TypeAlias, TypeVar
