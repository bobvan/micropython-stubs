"""
Control of WS2812 / NeoPixel LEDs.

MicroPython module: https://docs.micropython.org/en/v1.23.0-preview/library/neopixel.html

This module provides a driver for WS2818 / NeoPixel LEDs.

``Note:`` This module is only included by default on the ESP8266, ESP32 and RP2
   ports. On STM32 / Pyboard and others, you can either install the
   ``neopixel`` package using :term:`mip`, or you can download the module
   directly from :term:`micropython-lib` and copy it to the filesystem.

---
Module: 'neopixel' on micropython-v1.23.0-preview-esp32-ESP32_GENERIC
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': 'preview.176.g90e517862', 'arch': 'xtensawin', 'ver': '1.23.0-preview-preview.176.g90e517862', 'cpu': 'ESP32'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete
from typing import Tuple

def bitstream(*args, **kwargs) -> Incomplete: ...

class NeoPixel:
    """
    Construct an NeoPixel object.  The parameters are:

        - *pin* is a machine.Pin instance.
        - *n* is the number of LEDs in the strip.
        - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
        - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
    """

    ORDER: tuple = ()
    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
        ...
    def fill(self, pixel) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
