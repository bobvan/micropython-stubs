from _typeshed import Incomplete as Incomplete

PWRON_RESET: int
HARD_RESET: int
SOFT_RESET: int
WDT_RESET: int
DEEPSLEEP_RESET: int

def dht_readinto(*args, **kwargs) -> Incomplete: ...
def enable_irq(*args, **kwargs) -> Incomplete: ...
def disable_irq(*args, **kwargs) -> Incomplete: ...
def bitstream(*args, **kwargs) -> Incomplete: ...
def deepsleep(*args, **kwargs) -> Incomplete: ...
def bootloader(*args, **kwargs) -> Incomplete: ...
def reset_cause(*args, **kwargs) -> Incomplete: ...
def soft_reset(*args, **kwargs) -> Incomplete: ...
def freq(*args, **kwargs) -> Incomplete: ...
def reset(*args, **kwargs) -> Incomplete: ...
def time_pulse_us(*args, **kwargs) -> Incomplete: ...
def lightsleep(*args, **kwargs) -> Incomplete: ...
def idle(*args, **kwargs) -> Incomplete: ...
def unique_id(*args, **kwargs) -> Incomplete: ...

class WDT:
    def timeout_ms(self, *args, **kwargs) -> Incomplete: ...
    def feed(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

mem8: Incomplete
mem32: Incomplete
mem16: Incomplete

class PWM:
    def duty_u16(self, *args, **kwargs) -> Incomplete: ...
    def freq(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def duty_ns(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADC:
    def read_u16(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class DAC:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...
    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def writeto(self, *args, **kwargs) -> Incomplete: ...
    def writevto(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def readfrom(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Pin:
    OUT: int
    OPEN_DRAIN: int
    LOW_POWER: int
    PULL_DOWN: int
    PULL_OFF: int
    PULL_UP: int
    IRQ_RISING: int
    HIGH_POWER: int
    IN: int
    IRQ_FALLING: int
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def toggle(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def low(self, *args, **kwargs) -> Incomplete: ...
    def off(self, *args, **kwargs) -> Incomplete: ...
    def high(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def disable(self, *args, **kwargs) -> Incomplete: ...
    def drive(self, *args, **kwargs) -> Incomplete: ...

    class board:
        LCD_YU: Incomplete
        QSPI_SCK: Incomplete
        QSPI_D3: Incomplete
        QSPI_D2: Incomplete
        RX: Incomplete
        SCL1: Incomplete
        SCL0: Incomplete
        SCK: Incomplete
        QSPI_D1: Incomplete
        MIC: Incomplete
        LED_LCD: Incomplete
        LED_BLUE: Incomplete
        MISO: Incomplete
        QSPI_D0: Incomplete
        QSPI_CS: Incomplete
        MOSI: Incomplete
        SDA0: Incomplete
        SWITCH_X: Incomplete
        SWITCH_U: Incomplete
        SWITCH_B: Incomplete
        SWITCH_Y: Incomplete
        USB_DM: Incomplete
        TX: Incomplete
        SWITCH_Z: Incomplete
        SWDIO: Incomplete
        SD_DET: Incomplete
        SD_CS: Incomplete
        SDA1: Incomplete
        SD_MISO: Incomplete
        SWCLK: Incomplete
        SD_SCK: Incomplete
        SD_MOSI: Incomplete
        USB_DP: Incomplete
        LCD_YD: Incomplete
        BUTTON_2: Incomplete
        BUTTON_1: Incomplete
        A8_D8: Incomplete
        BUTTON_3: Incomplete
        ENABLE_3V3: Incomplete
        CS: Incomplete
        BUZZER: Incomplete
        A7_D7: Incomplete
        A2_D2: Incomplete
        A1_D1: Incomplete
        A0_D0: Incomplete
        A3_D3: Incomplete
        A6_D6: Incomplete
        A5_D5: Incomplete
        A4_D4: Incomplete
        ENABLE_5V: Incomplete
        LCD_MOSI: Incomplete
        LCD_MISO: Incomplete
        LCD_D_C: Incomplete
        LCD_RESET: Incomplete
        LCD_XR: Incomplete
        LCD_XL: Incomplete
        LCD_SCK: Incomplete
        LCD_CS: Incomplete
        GPCLK2: Incomplete
        GPCLK1: Incomplete
        GPCLK0: Incomplete
        I2C_BCLK: Incomplete
        I2S_SDOUT: Incomplete
        I2S_SDIN: Incomplete
        I2S_LRCLK: Incomplete
        def __init__(self, *argv, **kwargs) -> None: ...

    class cpu:
        PC04: Incomplete
        PC14: Incomplete
        PC05: Incomplete
        PC01: Incomplete
        PC03: Incomplete
        PC02: Incomplete
        PC12: Incomplete
        PC06: Incomplete
        PC13: Incomplete
        PC07: Incomplete
        PC11: Incomplete
        PC10: Incomplete
        PB24: Incomplete
        PC00: Incomplete
        PB25: Incomplete
        PB21: Incomplete
        PB23: Incomplete
        PB22: Incomplete
        PB30: Incomplete
        PB26: Incomplete
        PB31: Incomplete
        PB27: Incomplete
        PB29: Incomplete
        PB28: Incomplete
        PB20: Incomplete
        PD00: Incomplete
        PC15: Incomplete
        PD01: Incomplete
        PC28: Incomplete
        PC31: Incomplete
        PC30: Incomplete
        PD12: Incomplete
        PD08: Incomplete
        PD20: Incomplete
        PD09: Incomplete
        PD11: Incomplete
        PD10: Incomplete
        PC19: Incomplete
        PC27: Incomplete
        PC20: Incomplete
        PC16: Incomplete
        PC18: Incomplete
        PC17: Incomplete
        PC25: Incomplete
        PC21: Incomplete
        PC26: Incomplete
        PC22: Incomplete
        PC24: Incomplete
        PC23: Incomplete
        PD21: Incomplete
        PA15: Incomplete
        PA23: Incomplete
        PA16: Incomplete
        PA12: Incomplete
        PA14: Incomplete
        PA13: Incomplete
        PA21: Incomplete
        PA17: Incomplete
        PA22: Incomplete
        PA18: Incomplete
        PA20: Incomplete
        PA19: Incomplete
        PA03: Incomplete
        PA11: Incomplete
        PA04: Incomplete
        PA00: Incomplete
        PA02: Incomplete
        PA01: Incomplete
        PA09: Incomplete
        PA05: Incomplete
        PA10: Incomplete
        PA06: Incomplete
        PA08: Incomplete
        PA07: Incomplete
        PB19: Incomplete
        PB11: Incomplete
        PA24: Incomplete
        PB12: Incomplete
        PB08: Incomplete
        PB10: Incomplete
        PB09: Incomplete
        PB17: Incomplete
        PB13: Incomplete
        PB18: Incomplete
        PB14: Incomplete
        PB16: Incomplete
        PB15: Incomplete
        PA31: Incomplete
        PB07: Incomplete
        PB00: Incomplete
        PA25: Incomplete
        PA30: Incomplete
        PA27: Incomplete
        PB05: Incomplete
        PB01: Incomplete
        PB06: Incomplete
        PB02: Incomplete
        PB04: Incomplete
        PB03: Incomplete
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(self, *argv, **kwargs) -> None: ...

class SoftSPI:
    LSB: int
    MSB: int
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Timer:
    PERIODIC: int
    ONE_SHOT: int
    def init(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def txdone(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def sendbreak(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SoftI2C:
    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_into(self, *args, **kwargs) -> Incomplete: ...
    def readfrom_mem(self, *args, **kwargs) -> Incomplete: ...
    def writeto_mem(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def writeto(self, *args, **kwargs) -> Incomplete: ...
    def writevto(self, *args, **kwargs) -> Incomplete: ...
    def start(self, *args, **kwargs) -> Incomplete: ...
    def readfrom(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def stop(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RTC:
    def datetime(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def calibration(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class SPI:
    LSB: int
    MSB: int
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Signal:
    def off(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...