"""
Module: 'framebuf' on micropython-v1.22.2-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

MONO_HMSB: int = 4
MONO_HLSB: int = 3
RGB565: int = 1
MONO_VLSB: int = 0
MVLSB: int = 0
GS2_HMSB: int = 5
GS8: int = 6
GS4_HMSB: int = 2

def FrameBuffer1(*args, **kwargs) -> Incomplete: ...

class FrameBuffer:
    def poly(self, *args, **kwargs) -> Incomplete: ...
    def vline(self, *args, **kwargs) -> Incomplete: ...
    def pixel(self, *args, **kwargs) -> Incomplete: ...
    def text(self, *args, **kwargs) -> Incomplete: ...
    def rect(self, *args, **kwargs) -> Incomplete: ...
    def scroll(self, *args, **kwargs) -> Incomplete: ...
    def ellipse(self, *args, **kwargs) -> Incomplete: ...
    def line(self, *args, **kwargs) -> Incomplete: ...
    def blit(self, *args, **kwargs) -> Incomplete: ...
    def hline(self, *args, **kwargs) -> Incomplete: ...
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def fill_rect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...