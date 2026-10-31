""" """

from __future__ import annotations

from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

class WDT:
    """
    Create a WDT object and start it. The timeout must be given in milliseconds.
    Once it is running the timeout cannot be changed and the WDT cannot be stopped either.

    Notes:

    - On the alif port the HP and HE cores have independent watchdogs, both accessed
      by the default ``id=0``.  The maximum timeout on the HP core is 10737ms.  The
      watchdog does not run during deepsleep.

    - On the esp8266 port a timeout cannot be specified, it is determined by the underlying
      system.

    - On rp2040 devices the maximum timeout is 8388 ms.

    - On the stm32 port the default ``id=0`` is the IWDG, which can also be specified by
      an id of ``"IWDG"``.  Use an id of ``"WWDG"`` to access the WWDG peripheral.
      For dual-core STM32H7 MCUs there are also ``"IWDG2"`` and ``"WWDG2"``.
      The WWDG has a very limited maximum timeout across all MCUs, of around 100ms (but
      it depends heavily on the APB clock).
    """
    def __init__(self, id=0, timeout=5000) -> None: ...
    def feed(self) -> None:
        """
        Feed the WDT to prevent it from resetting the system. The application
        should place this call in a sensible place ensuring that the WDT is
        only fed after verifying that everything is functioning correctly.
        """
        ...
