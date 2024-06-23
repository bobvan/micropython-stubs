"""
Module: 'aioespnow' on micropython-v1.22.2-esp32-ESP32_GENERIC_S3
"""

# MCU: {'version': '1.22.2', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.22.2', 'cpu': 'ESP32S3'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class AIOESPNow:
    _data: list = []
    _none_tuple: tuple = ()
    def peer_count(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def mod_peer(self, *args, **kwargs) -> Incomplete: ...
    def irecv(self, *args, **kwargs) -> Incomplete: ...
    def stats(self, *args, **kwargs) -> Incomplete: ...
    def recvinto(self, *args, **kwargs) -> Incomplete: ...
    def set_pmk(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def add_peer(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def get_peers(self, *args, **kwargs) -> Incomplete: ...
    def get_peer(self, *args, **kwargs) -> Incomplete: ...
    def del_peer(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...

    asend: Generator  ## = <generator>
    arecv: Generator  ## = <generator>
    airecv: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
