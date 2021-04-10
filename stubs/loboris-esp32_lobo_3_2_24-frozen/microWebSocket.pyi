
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class MicroWebSocket:
    def _tryAllocByteArray(size: Any) -> Optional[Any]: ...
        #   0: return bytearray(size)
        # ? 0: return bytearray(size)
        #   1: return
        #   1: return
    def _tryStartThread(func: Any, args: Any=(), stackSize: Any=) -> Optional[Any]: ...
        #   0: return th
        # ? 0: return th
        #   1: return
        #   1: return
    def __init__(self, socket: Any, httpClient: Any, httpResponse: Any, maxRecvLen: Any, threaded: Any, acceptCallback: Any, stackSize: Any=) -> None: ...
    def _handshake(self, httpResponse: Any) -> None: ...
    def _wsProcess(self, acceptCallback: Any) -> None: ...
    def _receiveFrame(self) -> None: ...
    def _sendFrame(self, opcode: Any, data: Any=, fin: Any=) -> Optional[Any]: ...
        #   0: return ret
        # ? 0: return ret
        #   1: return
        #   1: return
    def SendText(self, msg: Any) -> Any: ...
        #   0: return self._sendFrame(self._opTextFrame,msg.encode())
        # ? 0: return self._sendFrame(self._opTextFrame, msg.encode())
    def SendBinary(self, data: Any) -> Any: ...
        #   0: return self._sendFrame(self._opBinFrame,data)
        # ? 0: return self._sendFrame(self._opBinFrame, data)
    def IsClosed(self) -> Any: ...
        #   0: return self._closed
        # ? 0: return self._closed
    def threadID(self) -> Any: ...
        #   0: return self.thID
        # ? 0: return self.thID
    def Close(self) -> None: ...
