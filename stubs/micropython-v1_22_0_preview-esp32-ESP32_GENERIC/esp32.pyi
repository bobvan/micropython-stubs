from _typeshed import Incomplete as Incomplete

WAKEUP_ALL_LOW: bool
WAKEUP_ANY_HIGH: bool
HEAP_EXEC: int
HEAP_DATA: int

def raw_temperature(*args, **kwargs) -> Incomplete: ...
def idf_heap_info(*args, **kwargs) -> Incomplete: ...
def wake_on_touch(*args, **kwargs) -> Incomplete: ...
def wake_on_ext0(*args, **kwargs) -> Incomplete: ...
def wake_on_ext1(*args, **kwargs) -> Incomplete: ...
def wake_on_ulp(*args, **kwargs) -> Incomplete: ...
def gpio_deep_sleep_hold(*args, **kwargs) -> Incomplete: ...

class ULP:
    RESERVE_MEM: int
    def run(self, *args, **kwargs) -> Incomplete: ...
    def set_wakeup_period(self, *args, **kwargs) -> Incomplete: ...
    def load_binary(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class NVS:
    def get_i32(self, *args, **kwargs) -> Incomplete: ...
    def set_i32(self, *args, **kwargs) -> Incomplete: ...
    def set_blob(self, *args, **kwargs) -> Incomplete: ...
    def commit(self, *args, **kwargs) -> Incomplete: ...
    def get_blob(self, *args, **kwargs) -> Incomplete: ...
    def erase_key(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Partition:
    RUNNING: int
    TYPE_APP: int
    TYPE_DATA: int
    BOOT: int
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def set_boot(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def find(self, *args, **kwargs) -> Incomplete: ...
    def get_next_update(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RMT:
    PULSE_MAX: int
    def source_freq(self, *args, **kwargs) -> Incomplete: ...
    def loop(self, *args, **kwargs) -> Incomplete: ...
    def wait_done(self, *args, **kwargs) -> Incomplete: ...
    def write_pulses(self, *args, **kwargs) -> Incomplete: ...
    def bitstream_channel(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def clock_div(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
