"""
Module: 'umqtt.robust' on micropython-v1.23.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.23.0', 'cpu': 'ESP8266'}
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
