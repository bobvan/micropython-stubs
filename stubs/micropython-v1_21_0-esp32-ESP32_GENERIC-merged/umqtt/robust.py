"""
Module: 'umqtt.robust' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete


class MQTTClient:
    DELAY = 2  # type: int
    DEBUG = False  # type: bool

    def ping(self, *args, **kwargs) -> Incomplete:
        ...

    def set_last_will(self, *args, **kwargs) -> Incomplete:
        ...

    def set_callback(self, *args, **kwargs) -> Incomplete:
        ...

    def subscribe(self, *args, **kwargs) -> Incomplete:
        ...

    def delay(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def check_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def reconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def publish(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
