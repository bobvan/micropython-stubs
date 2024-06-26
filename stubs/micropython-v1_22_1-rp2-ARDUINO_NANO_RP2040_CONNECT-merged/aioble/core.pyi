"""
Module: 'aioble.core' on micropython-v1.22.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'build': '', 'ver': '1.22.1', 'version': '1.22.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.16.3
from __future__ import annotations
from _typeshed import Incomplete

_irq_handlers: list = []
_shutdown_handlers: list = []
log_level: int = 1

def ensure_active(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def log_warn(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def log_info(*args, **kwargs) -> Incomplete: ...
def config(*args, **kwargs) -> Incomplete: ...
def stop(*args, **kwargs) -> Incomplete: ...
def ble_irq(*args, **kwargs) -> Incomplete: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class GattError(Exception): ...
