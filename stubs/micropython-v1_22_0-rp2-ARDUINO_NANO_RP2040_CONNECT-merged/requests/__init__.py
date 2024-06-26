"""
Module: 'requests.__init__' on micropython-v1.22.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def head(*args, **kwargs) -> Incomplete: ...


def delete(*args, **kwargs) -> Incomplete: ...


def patch(*args, **kwargs) -> Incomplete: ...


def post(*args, **kwargs) -> Incomplete: ...


def get(*args, **kwargs) -> Incomplete: ...


def request(*args, **kwargs) -> Incomplete: ...


def put(*args, **kwargs) -> Incomplete: ...


class Response:
    def json(self, *args, **kwargs) -> Incomplete: ...

    def close(self, *args, **kwargs) -> Incomplete: ...

    content: Incomplete  ## <class 'property'> = <property>
    text: Incomplete  ## <class 'property'> = <property>

    def __init__(self, *argv, **kwargs) -> None: ...
