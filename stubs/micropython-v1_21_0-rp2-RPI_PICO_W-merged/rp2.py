"""
Module: 'rp2' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Optional, Any
from _typeshed import Incomplete as Incomplete, Incomplete


def asm_pio(
    *,
    out_init: Incomplete | None = ...,
    set_init: Incomplete | None = ...,
    sideset_init: Incomplete | None = ...,
    in_shiftdir: int = ...,
    out_shiftdir: int = ...,
    autopush: bool = ...,
    autopull: bool = ...,
    push_thresh: int = ...,
    pull_thresh: int = ...,
    fifo_join=...,
) -> Incomplete:
    """
    Assemble a PIO program.

    The following parameters control the initial state of the GPIO pins, as one
    of `PIO.IN_LOW`, `PIO.IN_HIGH`, `PIO.OUT_LOW` or `PIO.OUT_HIGH`. If the
    program uses more than one pin, provide a tuple, e.g.
    ``out_init=(PIO.OUT_LOW, PIO.OUT_LOW)``.

    - *out_init* configures the pins used for ``out()`` instructions.
    - *set_init* configures the pins used for ``set()`` instructions. There can
      be at most 5.
    - *sideset_init* configures the pins used side-setting. There can be at
      most 5.

    The following parameters are used by default, but can be overridden in
    `StateMachine.init()`:

    - *in_shiftdir* is the default direction the ISR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *out_shiftdir* is the default direction the OSR will shift, either
      `PIO.SHIFT_LEFT` or `PIO.SHIFT_RIGHT`.
    - *push_thresh* is the threshold in bits before auto-push or conditional
      re-pushing is triggered.
    - *pull_thresh* is the threshold in bits before auto-pull or conditional
      re-pulling is triggered.

    The remaining parameters are:

    - *autopush* configures whether auto-push is enabled.
    - *autopull* configures whether auto-pull is enabled.
    - *fifo_join* configures whether the 4-word TX and RX FIFOs should be
      combined into a single 8-word FIFO for one direction only. The options
      are `PIO.JOIN_NONE`, `PIO.JOIN_RX` and `PIO.JOIN_TX`.
    """
    ...


def asm_pio_encode(instr, sideset_count, sideset_opt: bool = ...) -> Incomplete:
    """
    Assemble a single PIO instruction. You usually want to use `asm_pio()`
    instead.

    >>> rp2.asm_pio_encode("set(0, 1)", 0)
    57345
    """
    ...


def bootsel_button() -> Incomplete:
    """
    Temporarily turns the QSPI_SS pin into an input and reads its value,
    returning 1 for low and 0 for high.
    On a typical RP2040 board with a BOOTSEL button, a return value of 1
    indicates that the button is pressed.

    Since this function temporarily disables access to the external flash
    memory, it also temporarily disables interrupts and the other core to
    prevent them from trying to execute code from flash.
    """
    ...


def country(*args, **kwargs) -> Incomplete:
    ...


def const(*args, **kwargs) -> Incomplete:
    ...


class PIOASMEmit:
    def wrap(self, *args, **kwargs) -> Incomplete:
        ...

    def wait(self, *args, **kwargs) -> Incomplete:
        ...

    def jmp(self, *args, **kwargs) -> Incomplete:
        ...

    def word(self, *args, **kwargs) -> Incomplete:
        ...

    def in_(self, *args, **kwargs) -> Incomplete:
        ...

    def delay(self, *args, **kwargs) -> Incomplete:
        ...

    def start_pass(self, *args, **kwargs) -> Incomplete:
        ...

    def out(self, *args, **kwargs) -> Incomplete:
        ...

    def side(self, *args, **kwargs) -> Incomplete:
        ...

    def wrap_target(self, *args, **kwargs) -> Incomplete:
        ...

    def label(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def mov(self, *args, **kwargs) -> Incomplete:
        ...

    def push(self, *args, **kwargs) -> Incomplete:
        ...

    def pull(self, *args, **kwargs) -> Incomplete:
        ...

    def nop(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PIOASMError(Exception):
    """
    This exception is raised from `asm_pio()` or `asm_pio_encode()` if there is
    an error assembling a PIO program.
    """

    ...
