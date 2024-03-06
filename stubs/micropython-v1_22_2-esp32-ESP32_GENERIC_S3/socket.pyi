"""
Module: 'socket' on micropython-v1.22.2-esp32-ESP32_GENERIC_S3
"""
# MCU: {'version': '1.22.2', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.22.2', 'cpu': 'ESP32S3'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

SOCK_STREAM: int = 1
SOCK_DGRAM: int = 2
SOCK_RAW: int = 3
SO_BROADCAST: int = 32
SOL_SOCKET: int = 4095
SO_BINDTODEVICE: int = 4107
SO_REUSEADDR: int = 4
AF_INET6: int = 10
IP_ADD_MEMBERSHIP: int = 3
AF_INET: int = 2
IPPROTO_UDP: int = 17
IPPROTO_IP: int = 0
IPPROTO_TCP: int = 6

def getaddrinfo(*args, **kwargs) -> Incomplete: ...

class socket:
    def recvfrom(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def makefile(self, *args, **kwargs) -> Incomplete: ...
    def listen(self, *args, **kwargs) -> Incomplete: ...
    def fileno(self, *args, **kwargs) -> Incomplete: ...
    def sendall(self, *args, **kwargs) -> Incomplete: ...
    def setsockopt(self, *args, **kwargs) -> Incomplete: ...
    def setblocking(self, *args, **kwargs) -> Incomplete: ...
    def sendto(self, *args, **kwargs) -> Incomplete: ...
    def settimeout(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def bind(self, *args, **kwargs) -> Incomplete: ...
    def accept(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
