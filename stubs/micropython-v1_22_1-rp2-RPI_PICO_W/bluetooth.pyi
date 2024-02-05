"""
Module: 'bluetooth' on micropython-v1.22.1-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.1', 'build': '', 'ver': '1.22.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from _typeshed import Incomplete

FLAG_NOTIFY: int = 16
FLAG_READ: int = 2
FLAG_WRITE: int = 8
FLAG_INDICATE: int = 32
FLAG_WRITE_NO_RESPONSE: int = 4

class UUID:
    def __init__(self, *argv, **kwargs) -> None: ...

class BLE:
    def gatts_notify(self, *args, **kwargs) -> Incomplete: ...
    def gatts_indicate(self, *args, **kwargs) -> Incomplete: ...
    def gattc_write(self, *args, **kwargs) -> Incomplete: ...
    def gattc_read(self, *args, **kwargs) -> Incomplete: ...
    def gattc_exchange_mtu(self, *args, **kwargs) -> Incomplete: ...
    def gatts_read(self, *args, **kwargs) -> Incomplete: ...
    def gatts_write(self, *args, **kwargs) -> Incomplete: ...
    def gatts_set_buffer(self, *args, **kwargs) -> Incomplete: ...
    def gatts_register_services(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def gap_connect(self, *args, **kwargs) -> Incomplete: ...
    def gap_advertise(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_services(self, *args, **kwargs) -> Incomplete: ...
    def gap_disconnect(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_descriptors(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_characteristics(self, *args, **kwargs) -> Incomplete: ...
    def gap_scan(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
