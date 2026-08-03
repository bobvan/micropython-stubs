# Micropython v1.28.0 frozen stubs
from micropython import const as const

from .central import scan as scan
from .core import GattError as GattError
from .core import config as config
from .core import log_error as log_error
from .core import log_warn as log_warn
from .core import stop as stop
from .device import Device as Device
from .device import DeviceDisconnectedError as DeviceDisconnectedError
from .peripheral import advertise as advertise
from .server import BufferedCharacteristic as BufferedCharacteristic
from .server import Characteristic as Characteristic
from .server import Descriptor as Descriptor
from .server import Service as Service
from .server import register_services as register_services

ADDR_PUBLIC: int
ADDR_RANDOM: int
