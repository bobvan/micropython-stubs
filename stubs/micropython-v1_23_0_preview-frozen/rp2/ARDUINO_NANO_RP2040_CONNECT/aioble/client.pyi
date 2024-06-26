from .core import GattError as GattError, ble as ble, register_irq_handler as register_irq_handler
from .device import DeviceConnection as DeviceConnection
from _typeshed import Incomplete
from micropython import const as const

_IRQ_GATTC_SERVICE_RESULT: int
_IRQ_GATTC_SERVICE_DONE: int
_IRQ_GATTC_CHARACTERISTIC_RESULT: int
_IRQ_GATTC_CHARACTERISTIC_DONE: int
_IRQ_GATTC_DESCRIPTOR_RESULT: int
_IRQ_GATTC_DESCRIPTOR_DONE: int
_IRQ_GATTC_READ_RESULT: int
_IRQ_GATTC_READ_DONE: int
_IRQ_GATTC_WRITE_DONE: int
_IRQ_GATTC_NOTIFY: int
_IRQ_GATTC_INDICATE: int
_CCCD_UUID: int
_CCCD_NOTIFY: int
_CCCD_INDICATE: int
_FLAG_READ: int
_FLAG_WRITE_NO_RESPONSE: int
_FLAG_WRITE: int
_FLAG_NOTIFY: int
_FLAG_INDICATE: int

def _client_irq(event, data) -> None: ...

class ClientDiscover:
    _connection: Incomplete
    _queue: Incomplete
    _status: Incomplete
    _event: Incomplete
    _disc_type: Incomplete
    _parent: Incomplete
    _timeout_ms: Incomplete
    _args: Incomplete
    def __init__(self, connection, disc_type, parent, timeout_ms, *args) -> None: ...
    async def _start(self) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    def _discover_result(conn_handle, *args) -> None: ...
    def _discover_done(conn_handle, status) -> None: ...

class ClientService:
    connection: Incomplete
    _start_handle: Incomplete
    _end_handle: Incomplete
    uuid: Incomplete
    def __init__(self, connection, start_handle, end_handle, uuid) -> None: ...
    def __str__(self) -> str: ...
    async def characteristic(self, uuid, timeout_ms: int = 2000): ...
    def characteristics(self, uuid: Incomplete | None = None, timeout_ms: int = 2000): ...
    def _start_discovery(connection, uuid: Incomplete | None = None) -> None: ...

class BaseClientCharacteristic:
    _value_handle: Incomplete
    properties: Incomplete
    uuid: Incomplete
    _read_event: Incomplete
    _read_data: Incomplete
    _read_status: Incomplete
    _write_event: Incomplete
    _write_status: Incomplete
    def __init__(self, value_handle, properties, uuid) -> None: ...
    def _register_with_connection(self) -> None: ...
    def _find(conn_handle, value_handle): ...
    def _check(self, flag) -> None: ...
    async def read(self, timeout_ms: int = 1000): ...
    def _read_result(conn_handle, value_handle, data) -> None: ...
    def _read_done(conn_handle, value_handle, status) -> None: ...
    async def write(self, data, response: Incomplete | None = None, timeout_ms: int = 1000) -> None: ...
    def _write_done(conn_handle, value_handle, status) -> None: ...

class ClientCharacteristic(BaseClientCharacteristic):
    service: Incomplete
    connection: Incomplete
    _end_handle: Incomplete
    _notify_event: Incomplete
    _notify_queue: Incomplete
    _indicate_event: Incomplete
    _indicate_queue: Incomplete
    def __init__(self, service, end_handle, value_handle, properties, uuid) -> None: ...
    def __str__(self) -> str: ...
    def _connection(self): ...
    async def descriptor(self, uuid, timeout_ms: int = 2000): ...
    def descriptors(self, timeout_ms: int = 2000): ...
    def _start_discovery(service, uuid: Incomplete | None = None) -> None: ...
    async def _notified_indicated(self, queue, event, timeout_ms): ...
    async def notified(self, timeout_ms: Incomplete | None = None): ...
    def _on_notify_indicate(self, queue, event, data) -> None: ...
    def _on_notify(conn_handle, value_handle, notify_data) -> None: ...
    async def indicated(self, timeout_ms: Incomplete | None = None): ...
    def _on_indicate(conn_handle, value_handle, indicate_data) -> None: ...
    async def subscribe(self, notify: bool = True, indicate: bool = False) -> None: ...

class ClientDescriptor(BaseClientCharacteristic):
    characteristic: Incomplete
    def __init__(self, characteristic, dsc_handle, uuid) -> None: ...
    def __str__(self) -> str: ...
    def _connection(self): ...
    def _start_discovery(characteristic, uuid: Incomplete | None = None) -> None: ...
