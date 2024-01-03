"""
Module: 'esp32' on micropython-v1.22.0-esp32-ESP32_GENERIC
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

WAKEUP_ALL_LOW = False  # type: bool
WAKEUP_ANY_HIGH = True  # type: bool
HEAP_EXEC = 1  # type: int
HEAP_DATA = 4  # type: int


def raw_temperature(*args, **kwargs) -> Incomplete:
    ...


def idf_heap_info(*args, **kwargs) -> Incomplete:
    ...


def wake_on_touch(*args, **kwargs) -> Incomplete:
    ...


def wake_on_ext0(*args, **kwargs) -> Incomplete:
    ...


def wake_on_ext1(*args, **kwargs) -> Incomplete:
    ...


def wake_on_ulp(*args, **kwargs) -> Incomplete:
    ...


def gpio_deep_sleep_hold(*args, **kwargs) -> Incomplete:
    ...


class ULP:
    RESERVE_MEM = 2040  # type: int

    def run(self, *args, **kwargs) -> Incomplete:
        ...

    def set_wakeup_period(self, *args, **kwargs) -> Incomplete:
        ...

    def load_binary(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class NVS:
    def get_i32(self, *args, **kwargs) -> Incomplete:
        ...

    def set_i32(self, *args, **kwargs) -> Incomplete:
        ...

    def set_blob(self, *args, **kwargs) -> Incomplete:
        ...

    def commit(self, *args, **kwargs) -> Incomplete:
        ...

    def get_blob(self, *args, **kwargs) -> Incomplete:
        ...

    def erase_key(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Partition:
    RUNNING = 1  # type: int
    TYPE_APP = 0  # type: int
    TYPE_DATA = 1  # type: int
    BOOT = 0  # type: int

    def readblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def set_boot(self, *args, **kwargs) -> Incomplete:
        ...

    def writeblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def find(self, *args, **kwargs) -> Incomplete:
        ...

    def get_next_update(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class RMT:
    PULSE_MAX = 32767  # type: int

    def source_freq(self, *args, **kwargs) -> Incomplete:
        ...

    def loop(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_done(self, *args, **kwargs) -> Incomplete:
        ...

    def write_pulses(self, *args, **kwargs) -> Incomplete:
        ...

    def bitstream_channel(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def clock_div(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
