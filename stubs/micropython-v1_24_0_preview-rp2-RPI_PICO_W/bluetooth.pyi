"""
Module: 'bluetooth' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.62.g908ab1cec', 'ver': '1.24.0-preview-preview.62.g908ab1cec', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
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