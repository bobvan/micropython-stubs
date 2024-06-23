"""
Module: 'umqtt.robust' on micropython-v1.22.2-esp32-ESP32_GENERIC_S3
"""

# MCU: {'version': '1.22.2', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.22.2', 'cpu': 'ESP32S3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

class MQTTClient:
    DELAY: int = 2
    DEBUG: bool = False
    def subscribe(self, *args, **kwargs) -> Incomplete: ...
    def set_callback(self, *args, **kwargs) -> Incomplete: ...
    def set_last_will(self, *args, **kwargs) -> Incomplete: ...
    def delay(self, *args, **kwargs) -> Incomplete: ...
    def ping(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def _send_str(self, *args, **kwargs) -> Incomplete: ...
    def log(self, *args, **kwargs) -> Incomplete: ...
    def _recv_len(self, *args, **kwargs) -> Incomplete: ...
    def wait_msg(self, *args, **kwargs) -> Incomplete: ...
    def check_msg(self, *args, **kwargs) -> Incomplete: ...
    def reconnect(self, *args, **kwargs) -> Incomplete: ...
    def publish(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
