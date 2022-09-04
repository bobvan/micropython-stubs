from typing import Any

class MQTTClient:
    def __init__(self, *argv, **kwargs) -> None: ...
    def connect(self, *args, **kwargs) -> Any: ...
    def disconnect(self, *args, **kwargs) -> Any: ...
    def log(self, *args, **kwargs) -> Any: ...
    DEBUG: bool
    def set_callback(self, *args, **kwargs) -> Any: ...
    def set_last_will(self, *args, **kwargs) -> Any: ...
    def ping(self, *args, **kwargs) -> Any: ...
    publish: Any
    def subscribe(self, *args, **kwargs) -> Any: ...
    wait_msg: Any
    def check_msg(self, *args, **kwargs) -> Any: ...
    DELAY: int
    def delay(self, *args, **kwargs) -> Any: ...
    reconnect: Any