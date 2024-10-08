from micropython import const as const

VBUS_SENSE: int
VBAT_SENSE: int
LDO2: int
LED: int
AMB_LIGHT: int
RGB_DATA: int
RGB_PWR: int
RGB_MATRIX_DATA: int
RGB_MATRIX_PWR: int
SPI_MOSI: int
SPI_MISO: int
SPI_CLK: int
I2C_SDA: int
I2C_SCL: int

def led_set(state) -> None:
    """Set the state of the BLUE LED on IO13"""

def led_blink() -> None:
    """Toggle the BLUE LED on IO13"""

def get_amb_light():
    """Get Ambient Light Sensor reading"""

def set_ldo2_power(state) -> None:
    """
    Enable or Disable power to the second LDO, which is the LDO that powers the following items
    RGB Matrix, RGB status LED, Ambient light Sensor.
    This is ON by default and will automatically shut down when the ESP32 going into deep sleep.
    """

def get_battery_voltage():
    """
    Returns the current battery voltage. If no battery is connected, returns 4.2V which is the charge voltage
    This is an approximation only, but useful to detect if the charge state of the battery is getting low.
    """

def get_vbus_present():
    """Detect if VBUS (5V) power source is present"""

def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
