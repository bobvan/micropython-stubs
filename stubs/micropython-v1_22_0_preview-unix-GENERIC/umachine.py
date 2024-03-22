"""
Module: 'umachine' on micropython-v1.22.0.preview-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete


def idle(*args, **kwargs) -> Incomplete:
    ...


def soft_reset(*args, **kwargs) -> Incomplete:
    ...


def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...


mem8: Incomplete  ## <class 'mem'> = <8-bit memory>


class PinBase:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Signal:
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>