from _typeshed import Incomplete
from micropython import const as const

_LPS22_CTRL_REG1: int
_LPS22_CTRL_REG2: int
_LPS22_STATUS: int
_LPS22_TEMP_OUT_L: int
_LPS22_PRESS_OUT_XL: int
_LPS22_PRESS_OUT_L: int

class LPS22H:
    i2c: Incomplete
    addr: Incomplete
    oneshot: Incomplete
    buf: Incomplete
    def __init__(self, i2c, address: int = 92, oneshot: bool = False) -> None: ...
    def _int16(self, d): ...
    def _write_reg(self, reg, dat) -> None: ...
    def _read_reg(self, reg, width: int = 8): ...
    def _tigger_oneshot(self, b) -> None: ...
    def set_oneshot_mode(self, oneshot) -> None: ...
    def pressure(self): ...
    def temperature(self): ...
    def altitude(self): ...
