""" """

from __future__ import annotations

from typing import Any, Optional

from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

from .Pin import Pin

class Signal(Pin):
    """
            Signal(pin_arguments..., *, invert=False)

    Create a Signal object. There're two ways to create it:

    * By wrapping existing Pin object - universal method which works for
      any board.
    * By passing required Pin parameters directly to Signal constructor,
      skipping the need to create intermediate Pin object. Available on
      many, but not all boards.

    The arguments are:

      - ``pin_obj`` is existing Pin object.

      - ``pin_arguments`` are the same arguments as can be passed to Pin constructor.

      - ``invert`` - if True, the signal will be inverted (active low).

    .. note::
       The value of the pin can be set in the Pin constructor *and/or* the Signal constructor.
       If the Signal is also *inverted* then a value set in the *Pin* constructor will be in the opposite sense.

       Example::

         >>> c0 = Signal(Pin(0, Pin.OUT, value=0), invert=True)
         >>> c0()
         1
         >>> c1 = Signal(1, Pin.OUT, value=0, invert=True)
         >>> c1()
         0

       The first creates the pin and sets it's initial value and then Signal inverts the logic.
       Whereas, the second sets the pin to the inverted value.

       This behavior is only different after construction and before a call
       to a 'set' method.

       Example::

         >>> c0.off()
         >>> c0()
         0
         >>> c1.off()
         >>> c1()
         0
    """
    def __init__(self, pin_obj, *args, invert=False) -> None: ...
    def value(self, x: Optional[Any] = None) -> int:
        """
        This method allows to set and get the value of the signal, depending on whether
        the argument ``x`` is supplied or not.

        If the argument is omitted then this method gets the signal level, 1 meaning
        signal is asserted (active) and 0 - signal inactive.

        If the argument is supplied then this method sets the signal level. The
        argument ``x`` can be anything that converts to a boolean. If it converts
        to ``True``, the signal is active, otherwise it is inactive.

        Correspondence between signal being active and actual logic level on the
        underlying pin depends on whether signal is inverted (active-low) or not.
        For non-inverted signal, active status corresponds to logical 1, inactive -
        to logical 0. For inverted/active-low signal, active status corresponds
        to logical 0, while inactive - to logical 1.
        """
        ...
    def __call__(self, x: Optional[Any] = None) -> Incomplete:
        """
        Signal objects are callable.  The call method provides a (fast) shortcut to set
        and get the value of the pin.  It is equivalent to Signal.value([x]).
        See :meth:`Signal.value` for more details.
        """
        ...
    def on(self) -> None:
        """
        Activate signal.
        """
        ...
    def off(self) -> None:
        """
        Deactivate signal.
        """
        ...
