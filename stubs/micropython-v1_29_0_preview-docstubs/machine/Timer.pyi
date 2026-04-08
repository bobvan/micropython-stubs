""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable

class Timer:
    """
    Construct a new Timer object with the given ``id``.

    On ports which support virtual timers the ``id`` parameter is optional - the
    default value is ``-1`` which constructs a virtual timer.

    On ports which support hardware timers, setting the ``id`` parameter to a
    non-negative integer determines which timer to use.

    ``id`` shall not be passed as a keyword argument.

    Any additional parameters are handled the same as :func:`Timer.init()`.
    """

    ONE_SHOT: Incomplete
    """Timer operating mode."""
    PERIODIC: Incomplete
    """Timer operating mode."""
    def __init__(self, id=-1, *args, **kwargs) -> None: ...
    def init(self, *, mode=PERIODIC, freq=-1, period=-1, callback=None, hard=True) -> None:
        """
        Initialise the timer. Example::

            def mycallback(t):
                pass

            # periodic at 1kHz
            tim.init(mode=Timer.PERIODIC, freq=1000, callback=mycallback)

            # periodic with 100ms period
            tim.init(period=100, callback=mycallback)

            # one shot firing after 1000ms
            tim.init(mode=Timer.ONE_SHOT, period=1000, callback=mycallback)

        Keyword arguments:

          - ``mode`` can be one of:

            - ``Timer.ONE_SHOT`` - The timer runs once until the configured
              period of the channel expires.
            - ``Timer.PERIODIC`` - The timer runs periodically at the configured
              frequency of the channel.

          - ``freq`` - The timer frequency, in units of Hz.  The upper bound of
            the frequency is dependent on the port.  When both the ``freq`` and
            ``period`` arguments are given, ``freq`` has a higher priority and
            ``period`` is ignored.

          - ``period`` - The timer period, in milliseconds.

          - ``callback`` - The callable to call upon expiration of the timer period.
            The callback must take one argument, which is passed the Timer object.

            The ``callback`` argument shall be specified. Otherwise an exception
            will occur upon timer expiration:
            ``TypeError: 'NoneType' object isn't callable``

          - ``hard`` can be one of:

            - ``True`` - The callback will be executed in hard interrupt context,
              which minimises delay and jitter but is subject to the limitations
              described in :ref:`isr_rules`. Not all ports support hard interrupts,
              see the port documentation for more information.
            - ``False`` - The callback will be scheduled as a soft interrupt,
              allowing it to allocate but possibly also introducing
              garbage-collection delays and jitter.

            The default value of this parameter is port-specific for historical reasons.
        """
        ...
    def deinit(self) -> None:
        """
        Deinitialises the timer. Stops the timer, and disables the timer peripheral.
        """
        ...
