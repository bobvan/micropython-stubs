"""
Functionality specific to the ESP32.

MicroPython module: https://docs.micropython.org/en/preview.0/library/esp32.html

The ``esp32`` module contains functions and classes specifically aimed at
controlling ESP32 modules.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/esp32.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, Callable, List, Optional, Tuple, Union
from typing_extensions import TypeVar, TypeAlias, Awaitable

HEAP_DATA: Incomplete
"""Used in `idf_heap_info`."""
HEAP_EXEC: Incomplete
"""Used in `idf_heap_info`."""
WAKEUP_ALL_LOW: Incomplete
"""Selects the wake level for pins."""
WAKEUP_ANY_HIGH: Incomplete
"""Selects the wake level for pins."""

class Partition:
    """
    Create an object representing a partition.  *id* can be a string which is the label
    of the partition to retrieve, or one of the constants: ``BOOT`` or ``RUNNING``.
    *block_size* specifies the byte size of an individual block.
    """

    BOOT: Incomplete
    """\
    Used in the `Partition` constructor to fetch various partitions: ``BOOT`` is the
    partition that will be booted at the next reset and ``RUNNING`` is the currently
    running partition.
    """
    RUNNING: Incomplete
    """\
    Used in the `Partition` constructor to fetch various partitions: ``BOOT`` is the
    partition that will be booted at the next reset and ``RUNNING`` is the currently
    running partition.
    """
    TYPE_APP: Incomplete
    """\
    Used in `Partition.find` to specify the partition type: ``APP`` is for bootable
    firmware partitions (typically labelled ``factory``, ``ota_0``, ``ota_1``), and
    ``DATA`` is for other partitions, e.g. ``nvs``, ``otadata``, ``phy_init``, ``vfs``.
    """
    TYPE_DATA: Incomplete
    """\
    Used in `Partition.find` to specify the partition type: ``APP`` is for bootable
    firmware partitions (typically labelled ``factory``, ``ota_0``, ``ota_1``), and
    ``DATA`` is for other partitions, e.g. ``nvs``, ``otadata``, ``phy_init``, ``vfs``.
    """
    def __init__(self, id, block_size=4096, /) -> None: ...
    @classmethod
    def find(cls, type=TYPE_APP, subtype=0xFF, label=None, block_size=4096) -> List:
        """
        Find a partition specified by *type*, *subtype* and *label*.  Returns a
        (possibly empty) list of Partition objects. Note: ``subtype=0xff`` matches any subtype
        and ``label=None`` matches any label.

        *block_size* specifies the byte size of an individual block used by the returned
        objects.
        """
        ...
    def info(self) -> Tuple:
        """
        Returns a 6-tuple ``(type, subtype, addr, size, label, encrypted)``.
        """
        ...
    def readblocks(self, block_num, buf, offset: Optional[int] = 0) -> None: ...
    def writeblocks(self, block_num, buf, offset: Optional[int] = 0) -> None: ...
    def ioctl(self, cmd, arg) -> Incomplete:
        """
        These methods implement the simple and :ref:`extended
        <block-device-interface>` block protocol defined by
        :class:`vfs.AbstractBlockDev`.
        """
        ...
    def set_boot(self) -> None:
        """
        Sets the partition as the boot partition.

        ``Note:`` Do not enter :func:`deepsleep<machine.deepsleep>` after changing
           the OTA boot partition, without first performing a hard
           :func:`reset<machine.reset>` or power cycle. This ensures the bootloader
           will validate the new image before booting.
        """
        ...
    def get_next_update(self) -> Partition:
        """
        Gets the next update partition after this one, and returns a new Partition object.
        Typical usage is ``Partition(Partition.RUNNING).get_next_update()``
        which returns the next partition to update given the current running one.
        """
        ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls) -> Incomplete:
        """
        Signals that the current boot is considered successful.
        Calling ``mark_app_valid_cancel_rollback`` is required on the first boot of a new
        partition to avoid an automatic rollback at the next boot.
        This uses the ESP-IDF "app rollback" feature with "CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE"
        and  an ``OSError(-261)`` is raised if called on firmware that doesn't have the
        feature enabled.
        It is OK to call ``mark_app_valid_cancel_rollback`` on every boot and it is not
        necessary when booting firmware that was loaded using esptool.
        """
        ...

class PCNT:
    """
    Returns the singleton PCNT instance for the given unit ``id``.

    Keyword arguments are passed to the ``init()`` method as described
    below.
    """
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, *args, **kwargs) -> Incomplete:
        """
        (Re-)initialise a pulse counter unit. Supported keyword arguments are:

          - ``channel``: see description below
          - ``pin``: the input Pin to monitor for pulses
          - ``rising``: an action to take on a rising edge - one of
            ``PCNT.INCREMENT``, ``PCNT.DECREMENT`` or ``PCNT.IGNORE`` (the default)
          - ``falling``: an action to take on a falling edge (takes the save values
            as the ``rising`` argument).
          - ``mode_pin``: ESP32 pulse counters support monitoring a second pin and
            altering the behaviour of the counter based on its level - set this
            keyword to any input Pin
          - ``mode_low``: set to either ``PCNT.HOLD`` or ``PCNT.REVERSE`` to
            either suspend counting or reverse the direction of the counter (i.e.,
            ``PCNT.INCREMENT`` behaves as ``PCNT.DECREMENT`` and vice versa)
            when ``mode_pin`` is low
          - ``mode_high``: as ``mode_low`` but for the behaviour when ``mode_pin``
            is high
          - ``filter``: set to a value 1..1023, in ticks of the 80MHz clock, to
            enable the pulse width filter
          - ``min``: set to the minimum level of the counter value when
            decrementing (-32768..-1) or 0 to disable
          - ``max``: set to the maximum level of the counter value when
            incrementing (1..32767) or 0 to disable
          - ``threshold0``: sets the counter value for the
            ``PCNT.IRQ_THRESHOLD0`` event (see ``irq`` method)
          - ``threshold1``: sets the counter value for the
            ``PCNT.IRQ_THRESHOLD1`` event (see ``irq`` method)
          - ``value``: can be set to ``0`` to reset the counter value

        The hardware initialisation is done in stages and so some of the keyword
        arguments can be used in groups or in isolation to partially reconfigure a
        unit:

          - the ``pin`` keyword (optionally combined with ``mode_pin``) can be used
            to change just the bound pin(s)
          - ``rising``, ``falling``, ``mode_low`` and ``mode_high`` can be used
            (singly or together) to change the counting logic - omitted keywords
            use their default (``PCNT.IGNORE`` or ``PCNT.NORMAL``)
          - ``filter`` can be used to change only the pulse width filter (with 0
            disabling it)
          - each of ``min``, ``max``, ``threshold0`` and ``threshold1`` can
            be used to change these limit/event values individually; however,
            setting any will reset the counter to zero (i.e., they imply
            ``value=0``)

        Each pulse counter unit supports two channels, 0 and 1, each able to
        monitor different pins with different counting logic but updating the same
        counter value. Use ``channel=1`` with the ``pin``, ``rising``, ``falling``,
        ``mode_pin``, ``mode_low`` and ``mode_high`` keywords to configure the
        second channel.

        The second channel can be used to configure 4X quadrature decoding with a
        single counter unit::

            pin_a = Pin(2, Pin.INPUT, pull=Pin.PULL_UP)
            pin_b = Pin(3, Pin.INPUT, pull=Pin.PULL_UP)
            rotary = PCNT(0, min=-32000, max=32000)
            rotary.init(channel=0, pin=pin_a, falling=PCNT.INCREMENT, rising=PCNT.DECREMENT, mode_pin=pin_b, mode_low=PCNT.REVERSE)
            rotary.init(channel=1, pin=pin_b, falling=PCNT.DECREMENT, rising=PCNT.INCREMENT, mode_pin=pin_a, mode_low=PCNT.REVERSE)
            rotary.start()
        """
        ...
    def value(self, value: Optional[Any] = None) -> Incomplete:
        """
        Call this method with no arguments to return the current counter value.

        If the optional *value* argument is set to ``0`` then the counter is
        reset (but the previous value is returned). Read and reset is not atomic and
        so it is possible for a pulse to be missed. Any value other than ``0`` will
        raise an error.
        """
        ...
    def irq(self, handler=None, trigger=IRQ_ZERO) -> Callable[..., Incomplete]:
        """
        ESP32 pulse counters support interrupts on these counter events:

          - ``PCNT.IRQ_ZERO``: the counter has reset to zero
          - ``PCNT.IRQ_MIN``: the counter has hit the ``min`` value
          - ``PCNT.IRQ_MAX``: the counter has hit the ``max`` value
          - ``PCNT.IRQ_THRESHOLD0``: the counter has hit the ``threshold0`` value
          - ``PCNT.IRQ_THRESHOLD1``: the counter has hit the ``threshold1`` value

        ``trigger`` should be a bit-mask of the desired events OR'ed together. The
        ``handler`` function should take a single argument which is the
        :class:`PCNT` instance that raised the event.

        This method returns a callback object. The callback object can be used to
        access the bit-mask of events that are outstanding on the PCNT unit.::

            def pcnt_irq(pcnt):
                flags = pcnt.irq().flags()
                if flags & PCNT.IRQ_ZERO:
                   # reset
                if flags & PCNT.IRQ_MAX:
                   # overflow...
        """
        ...

class RMT:
    """
    This class provides access to one of the eight RMT channels. *channel* is
    required and identifies which RMT channel (0-7) will be configured. *pin*,
    also required, configures which Pin is bound to the RMT channel. *clock_div*
    is an 8-bit clock divider that divides the source clock (80MHz) to the RMT
    channel allowing the resolution to be specified. *idle_level* specifies
    what level the output will be when no transmission is in progress and can
    be any value that converts to a boolean, with ``True`` representing high
    voltage and ``False`` representing low.

    To enable the transmission carrier feature, *tx_carrier* should be a tuple
    of three positive integers: carrier frequency, duty percent (``0`` to
    ``100``) and the output level to apply the carrier to (a boolean as per
    *idle_level*).
    """

    PULSE_MAX: int
    """Maximum integer that can be set for a pulse duration."""
    def __init__(self, channel, *, pin=None, clock_div=8, idle_level=False, tx_carrier=None) -> None: ...
    @classmethod
    def source_freq(cls) -> Incomplete:
        """
        Returns the source clock frequency. Currently the source clock is not
        configurable so this will always return 80MHz.
        """
        ...
    def clock_div(self) -> Incomplete:
        """
        Return the clock divider. Note that the channel resolution is
        ``1 / (source_freq / clock_div)``.
        """
        ...
    def wait_done(self, *, timeout=0) -> bool:
        """
        Returns ``True`` if the channel is idle or ``False`` if a sequence of
        pulses started with `RMT.write_pulses` is being transmitted. If the
        *timeout* keyword argument is given then block for up to this many
        milliseconds for transmission to complete.
        """
        ...
    def loop(self, enable_loop) -> None:
        """
        Configure looping on the channel. *enable_loop* is bool, set to ``True`` to
        enable looping on the *next* call to `RMT.write_pulses`. If called with
        ``False`` while a looping sequence is currently being transmitted then the
        current loop iteration will be completed and then transmission will stop.
        """
        ...
    def write_pulses(self, duration, data: Union[bool, int] = True) -> Incomplete:
        """
        Begin transmitting a sequence. There are three ways to specify this:

        **Mode 1:** *duration* is a list or tuple of durations. The optional *data*
        argument specifies the initial output level. The output level will toggle
        after each duration.

        **Mode 2:** *duration* is a positive integer and *data* is a list or tuple
        of output levels. *duration* specifies a fixed duration for each.

        **Mode 3:** *duration* and *data* are lists or tuples of equal length,
        specifying individual durations and the output level for each.

        Durations are in integer units of the channel resolution (as
        described above), between 1 and ``PULSE_MAX`` units. Output levels
        are any value that can be converted to a boolean, with ``True``
        representing high voltage and ``False`` representing low.

        If transmission of an earlier sequence is in progress then this method will
        block until that transmission is complete before beginning the new sequence.

        If looping has been enabled with `RMT.loop`, the sequence will be
        repeated indefinitely. Further calls to this method will block until the
        end of the current loop iteration before immediately beginning to loop the
        new sequence of pulses. Looping sequences longer than 126 pulses is not
        supported by the hardware.
        """
        ...
    @staticmethod
    def bitstream_channel(value: Optional[Any] = None) -> int:
        """
        Select which RMT channel is used by the `machine.bitstream` implementation.
        *value* can be ``None`` or a valid RMT channel number.  The default RMT
        channel is the highest numbered one.

        Passing in ``None`` disables the use of RMT and instead selects a bit-banging
        implementation for `machine.bitstream`.

        Passing in no argument will not change the channel.  This function returns
        the current channel number.
        """
        ...

class ULP:
    """
    This class provides access to the Ultra-Low-Power co-processor.
    """
    def __init__(self) -> None: ...
    def set_wakeup_period(self, period_index, period_us) -> None:
        """
        Set the wake-up period.
        """
        ...
    def load_binary(self, load_addr, program_binary) -> None:
        """
        Load a *program_binary* into the ULP at the given *load_addr*.
        """
        ...
    def run(self, entry_point) -> Incomplete:
        """
        Start the ULP running at the given *entry_point*.
        """
        ...

class NVS:
    """
    Create an object providing access to a namespace (which is automatically created if not
    present).
    """
    def __init__(self, namespace) -> None: ...
    def set_i32(self, key, value) -> None:
        """
        Sets a 32-bit signed integer value for the specified key. Remember to call *commit*!
        """
        ...
    def get_i32(self, key) -> int:
        """
        Returns the signed integer value for the specified key. Raises an OSError if the key does not
        exist or has a different type.
        """
        ...
    def set_blob(self, key, value) -> None:
        """
        Sets a binary blob value for the specified key. The value passed in must support the buffer
        protocol, e.g. bytes, bytearray, str. (Note that esp-idf distinguishes blobs and strings, this
        method always writes a blob even if a string is passed in as value.)
        Remember to call *commit*!
        """
        ...
    def get_blob(self, key, buffer) -> int:
        """
        Reads the value of the blob for the specified key into the buffer, which must be a bytearray.
        Returns the actual length read. Raises an OSError if the key does not exist, has a different
        type, or if the buffer is too small.
        """
        ...
    def erase_key(self, key) -> Incomplete:
        """
        Erases a key-value pair.
        """
        ...
    def commit(self) -> Incomplete:
        """
        Commits changes made by *set_xxx* methods to flash.
        """
        ...

def wake_on_touch(wake) -> None:
    """
    Configure whether or not a touch will wake the device from sleep.
    *wake* should be a boolean value.

    ``Note:`` This is only available for boards that have touch sensor support.
    """
    ...

def wake_on_ulp(wake) -> None:
    """
    Configure whether or not the Ultra-Low-Power co-processor can wake the
    device from sleep. *wake* should be a boolean value.

    ``Note:`` This is only available for boards that have ULP coprocessor support.
    """
    ...

def wake_on_ext0(pin, level) -> None:
    """
    Configure how EXT0 wakes the device from sleep.  *pin* can be ``None``
    or a valid Pin object.  *level* should be ``esp32.WAKEUP_ALL_LOW`` or
    ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` This is only available for boards that have ext0 support.
    """
    ...

def wake_on_ext1(pins, level) -> None:
    """
    Configure how EXT1 wakes the device from sleep.  *pins* can be ``None``
    or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
    or ``esp32.WAKEUP_ANY_HIGH``.

    ``Note:`` This is only available for boards that have ext1 support.
    """
    ...

def gpio_deep_sleep_hold(enable) -> None:
    """
    Configure whether non-RTC GPIO pin configuration is retained during
    deep-sleep mode for held pads. *enable* should be a boolean value.
    """
    ...

def raw_temperature() -> int:
    """
    Read the raw value of the internal temperature sensor, returning an integer.
    """
    ...

def idf_heap_info(capabilities) -> List[Tuple]:
    """
    Returns information about the ESP-IDF heap memory regions. One of them contains
    the MicroPython heap and the others are used by ESP-IDF, e.g., for network
    buffers and other data. This data is useful to get a sense of how much memory
    is available to ESP-IDF and the networking stack in particular. It may shed
    some light on situations where ESP-IDF operations fail due to allocation failures.

    The capabilities parameter corresponds to ESP-IDF's ``MALLOC_CAP_XXX`` values but the
    two most useful ones are predefined as `esp32.HEAP_DATA` for data heap regions and
    `esp32.HEAP_EXEC` for executable regions as used by the native code emitter.

    The return value is a list of 4-tuples, where each 4-tuple corresponds to one heap
    and contains: the total bytes, the free bytes, the largest free block, and
    the minimum free seen over time.

    Example after booting::

        >>> import esp32; esp32.idf_heap_info(esp32.HEAP_DATA)
        [(240, 0, 0, 0), (7288, 0, 0, 0), (16648, 4, 4, 4), (79912, 35712, 35512, 35108),
         (15072, 15036, 15036, 15036), (113840, 0, 0, 0)]

    ``Note:`` Free IDF heap memory in the `esp32.HEAP_DATA` region is available
       to be automatically added to the MicroPython heap to prevent a
       MicroPython allocation from failing. However, the information returned
       here is otherwise *not* useful to troubleshoot Python allocation
       failures. :func:`micropython.mem_info()` and :func:`gc.mem_free()` should
       be used instead:

       The "max new split" value in :func:`micropython.mem_info()` output
       corresponds to the largest free block of ESP-IDF heap that could be
       automatically added on demand to the MicroPython heap.

       The result of :func:`gc.mem_free()` is the total of the current "free"
       and "max new split" values printed by :func:`micropython.mem_info()`.
    """
    ...

def idf_task_info() -> Tuple:
    """
    Returns information about running ESP-IDF/FreeRTOS tasks, which include
    MicroPython threads. This data is useful to gain insight into how much time
    tasks spend running or if they are blocked for significant parts of time,
    and to determine if allocated stacks are fully utilized or might be reduced.

    ``CONFIG_FREERTOS_USE_TRACE_FACILITY=y`` must be set in the board
    configuration to make this method available. Additionally configuring
    ``CONFIG_FREERTOS_GENERATE_RUN_TIME_STATS=y`` and
    ``CONFIG_FREERTOS_VTASKLIST_INCLUDE_COREID=y`` is recommended to be able to
    retrieve the total and per-task runtime and the core ID respectively.

    The return value is a 2-tuple where the first value is the total runtime,
    and the second a list of tasks. Each task is a 7-tuple containing: the task
    ID, name, current state, priority, runtime, stack high water mark, and the
    ID of the core it is running on. Runtime and core ID will be None when the
    respective FreeRTOS configuration option is not enabled.

    ``Note:`` For an easier to use output based on this function you can use the
       `utop library <https://github.com/micropython/micropython-lib/tree/master/micropython/utop>`_,
       which implements a live overview similar to the Unix ``top`` command.
    """
    ...
