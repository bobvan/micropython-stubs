"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/asyncio.html

CPython module:
`asyncio `<https://docs.python.org/3.8/library/asyncio.html>

Example::

    import asyncio

    async def blink(led, period_ms):
        while True:
            led.on()
            await asyncio.sleep_ms(5)
            led.off()
            await asyncio.sleep_ms(period_ms)

    async def main(led1, led2):
        asyncio.create_task(blink(led1, 700))
        asyncio.create_task(blink(led2, 400))
        await asyncio.sleep_ms(10_000)

    # Running on a pyboard
    from pyb import LED
    asyncio.run(main(LED(1), LED(2)))

    # Running on a generic board
    from machine import Pin
    asyncio.run(main(Pin(1), Pin(2)))

Core functions
--------------

---
Module: 'uasyncio.__init__' on micropython-v1.21.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.21.0', 'cpu': 'ESP8266'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Coroutine, List, Tuple
