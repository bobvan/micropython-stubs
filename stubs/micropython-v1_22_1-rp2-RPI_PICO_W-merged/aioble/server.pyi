"""
Module: 'aioble.server' on micropython-v1.22.1-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.1', 'build': '', 'ver': '1.22.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

_registered_characteristics: dict = {}

def _server_shutdown(*args, **kwargs) -> Incomplete: ...
def ensure_active(*args, **kwargs) -> Incomplete: ...
def _server_irq(*args, **kwargs) -> Incomplete: ...
def register_services(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def log_warn(*args, **kwargs) -> Incomplete: ...
def log_info(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class BaseCharacteristic:
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def _register(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class BufferedCharacteristic:
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def _indicate_done(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    def _register(self, *args, **kwargs) -> Incomplete: ...

    indicate: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class deque:
    def popleft(self, *args, **kwargs) -> Incomplete: ...
    def append(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceTimeout:
    _timeout_sleep: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Service:
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class GattError(Exception): ...

class Characteristic:
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def _register(self, *args, **kwargs) -> Incomplete: ...
    def _indicate_done(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    indicate: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceConnection:
    _connected: dict = {}
    def is_connected(self, *args, **kwargs) -> Incomplete: ...
    def _run_task(self, *args, **kwargs) -> Incomplete: ...
    def services(self, *args, **kwargs) -> Incomplete: ...
    def timeout(self, *args, **kwargs) -> Incomplete: ...

    device_task: Generator  ## = <generator>
    l2cap_connect: Generator  ## = <generator>
    pair: Generator  ## = <generator>
    service: Generator  ## = <generator>
    l2cap_accept: Generator  ## = <generator>
    disconnected: Generator  ## = <generator>
    exchange_mtu: Generator  ## = <generator>
    disconnect: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Descriptor:
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _remote_read(self, *args, **kwargs) -> Incomplete: ...
    def _remote_write(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def _register(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def _init_capture(self, *args, **kwargs) -> Incomplete: ...

    written: Generator  ## = <generator>
    _run_capture_task: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
