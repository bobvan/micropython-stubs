"""
Module: '_asyncio' on micropython-v1.23.0-stm32-PYBV11
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.23.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

class TaskQueue:
    def push(self, *args, **kwargs) -> Incomplete: ...
    def peek(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def pop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...
