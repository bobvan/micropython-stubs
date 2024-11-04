from _typeshed import Incomplete as Incomplete

class OneWire:
    MATCH_ROM: int
    SKIP_ROM: int
    SEARCH_ROM: int
    def select_rom(self, *args, **kwargs) -> Incomplete: ...
    def writebyte(self, *args, **kwargs) -> Incomplete: ...
    def crc8(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readbyte(self, *args, **kwargs) -> Incomplete: ...
    def readbit(self, *args, **kwargs) -> Incomplete: ...
    def writebit(self, *args, **kwargs) -> Incomplete: ...
    def reset(self, *args, **kwargs) -> Incomplete: ...
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class OneWireError(Exception): ...
