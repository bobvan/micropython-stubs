from _typeshed import Incomplete
from micropython import const as const

_DEBUG: bool

def _clamp(v, vmin, vmax): ...
def _flag(value, condition): ...

class ConfigError(ValueError):
    def __init__(self, field) -> None: ...

class BaseModem:
    _ant_sw: Incomplete
    _irq_callback: Incomplete
    _rf_freq_hz: int
    _sf: int
    _bw_hz: int
    _coding_rate: int
    _crc_en: bool
    _implicit_header: bool
    _preamble_len: int
    crc_errors: int
    rx_crc_error: bool
    _rx: bool
    _rx_continuous: bool
    _rx_length: Incomplete
    _tx: bool
    _last_irq: Incomplete
    _invert_iq: Incomplete
    def __init__(self, ant_sw) -> None: ...
    def standby(self) -> None: ...
    def _get_t_sym_us(self): ...
    def _get_ldr_en(self): ...
    def _get_pa_ramp_val(self, lora_cfg, supported): ...
    def _symbol_offsets(self): ...
    def get_n_symbols_x4(self, payload_len): ...
    def get_time_on_air_us(self, payload_len): ...
    def _radio_isr(self, _) -> None: ...
    def irq_triggered(self): ...
    def set_irq_callback(self, callback) -> None: ...
    def _get_last_irq(self): ...
    def start_recv(self, timeout_ms: Incomplete | None = None, continuous: bool = False, rx_length: int = 255) -> None: ...
    def poll_recv(self, rx_packet: Incomplete | None = None): ...
    def _end_recv(self) -> None: ...
    def _check_recv(self): ...
    def poll_send(self): ...

class RxPacket(bytearray):
    ticks_ms: Incomplete
    snr: Incomplete
    rssi: Incomplete
    valid_crc: Incomplete
    def __init__(
        self,
        payload,
        ticks_ms: Incomplete | None = None,
        snr: Incomplete | None = None,
        rssi: Incomplete | None = None,
        valid_crc: bool = True,
    ) -> None: ...
    def __repr__(self) -> str: ...
