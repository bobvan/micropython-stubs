"""
Input/output streams.

MicroPython module: https://docs.micropython.org/en/v1.29.0/library/io.html

CPython module: :mod:`python:io` https://docs.python.org/3/library/io.html .

This module contains additional types of `stream` (file-like) objects
and helper functions.

Conceptual hierarchy
--------------------

Admonition:Difference to CPython
   :class: attention

   Conceptual hierarchy of stream base classes is simplified in MicroPython,
   as described in this section.

(Abstract) base stream classes, which serve as a foundation for behaviour
of all the concrete classes, adhere to few dichotomies (pair-wise
classifications) in CPython. In MicroPython, they are somewhat simplified
and made implicit to achieve higher efficiencies and save resources.

An important dichotomy in CPython is unbuffered vs buffered streams. In
MicroPython, all streams are currently unbuffered. This is because all
modern OSes, and even many RTOSes and filesystem drivers already perform
buffering on their side. Adding another layer of buffering is counter-
productive (an issue known as "bufferbloat") and takes precious memory.
Note that there still cases where buffering may be useful, so we may
introduce optional buffering support at a later time.

But in CPython, another important dichotomy is tied with "bufferedness" -
it's whether a stream may incur short read/writes or not. A short read
is when a user asks e.g. 10 bytes from a stream, but gets less, similarly
for writes. In CPython, unbuffered streams are automatically short
operation susceptible, while buffered are guarantee against them. The
no short read/writes is an important trait, as it allows to develop
more concise and efficient programs - something which is highly desirable
for MicroPython. So, while MicroPython doesn't support buffered streams,
it still provides for no-short-operations streams. Whether there will
be short operations or not depends on each particular class' needs, but
developers are strongly advised to favour no-short-operations behaviour
for the reasons stated above. For example, MicroPython sockets are
guaranteed to avoid short read/writes. Actually, at this time, there is
no example of a short-operations stream class in the core, and one would
be a port-specific class, where such a need is governed by hardware
peculiarities.

The no-short-operations behaviour gets tricky in case of non-blocking
streams, blocking vs non-blocking behaviour being another CPython dichotomy,
fully supported by MicroPython. Non-blocking streams never wait for
data either to arrive or be written - they read/write whatever possible,
or signal lack of data (or ability to write data). Clearly, this conflicts
with "no-short-operations" policy, and indeed, a case of non-blocking
buffered (and this no-short-ops) streams is convoluted in CPython - in
some places, such combination is prohibited, in some it's undefined or
just not documented, in some cases it raises verbose exceptions. The
matter is much simpler in MicroPython: non-blocking stream are important
for efficient asynchronous operations, so this property prevails on
the "no-short-ops" one. So, while blocking streams will avoid short
reads/writes whenever possible (the only case to get a short read is
if end of file is reached, or in case of error (but errors don't
return short data, but raise exceptions)), non-blocking streams may
produce short data to avoid blocking the operation.

The final dichotomy is binary vs text streams. MicroPython of course
supports these, but while in CPython text streams are inherently
buffered, they aren't in MicroPython. (Indeed, that's one of the cases
for which we may introduce buffering support.)

Note that for efficiency, MicroPython doesn't provide abstract base
classes corresponding to the hierarchy above.  However, the
:class:`IOBase` class can be subclassed to implement custom stream
objects in pure Python.
"""

# source version: v1.29.0
# origin module:: repos/micropython/docs/library/io.rst
from __future__ import annotations

from typing import IO, Any, Optional

from _mpy_shed import AnyReadableBuf, AnyWritableBuf, IOBase_mp
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

class IOBase(IOBase_mp):
    """
    Base class for implementing custom stream objects in Python. Subclasses
    can override ``readinto``, ``write``, and ``ioctl`` to create objects
    that work with ``print()``, ``json.dump()``, ``select.poll()``,
    ``open()`` via a user filesystem, and other stream consumers.

    Admonition:Difference to CPython
       :class: attention

       In CPython, ``io.IOBase`` has a much larger API surface. MicroPython's
       ``IOBase`` is minimal: the C stream infrastructure provides standard
       methods like ``read()``, ``readline()``, ``seek()``, ``close()``, and
       ``flush()`` automatically. Subclasses only need to implement the
       methods below.

    Subclasses implement some or all of the following methods. The C stream
    layer calls these internally when user code calls standard stream
    functions.
    """
    def __init__(self) -> None: ...
    def readinto(self, buf) -> int:
        """
        Read data into *buf* (a ``bytearray`` sized by the caller). Return the
        number of bytes read, 0 at EOF, or ``None`` if no data is available on
        a non-blocking stream. Return a negative errno value (e.g. ``-errno.EIO``
        or ``-1``) to signal an error.
        """
        ...
    def write(self, buf) -> int:
        """
        Write *buf* (a ``bytearray``) to the stream. Return the number of
        bytes written, or ``None`` if a non-blocking stream cannot accept data.
        Return a negative errno value to signal an error.
        """
        ...
    def ioctl(self, op, arg) -> int:
        """
        Control the stream and query its properties. The operation to perform
        is given by *op* which is one of the following integers:

          - 1 -- flush write buffers (*arg* is unused)
          - 3 -- poll for readiness; *arg* is a bitmask of events to check,
            return a bitmask of ready events. Poll flags:

            * ``0x0001`` -- data available for reading
            * ``0x0004`` -- stream ready for writing
            * ``0x0008`` -- error condition
            * ``0x0010`` -- hang up (e.g. connection closed)
            * ``0x0020`` -- invalid request

          - 4 -- close the stream (*arg* is unused)
          - 11 -- return the preferred read buffer size, or 0 (*arg* is unused)

        As a minimum ``ioctl(4, ...)`` should be handled to support stream
        closure. Implement ``ioctl(3, ...)`` if the stream will be used with
        ``select.poll()`` or ``asyncio``.

        Other operations exist for advanced use cases (2 = seek, 5 = timeout,
        10 = fileno); see ``py/stream.h`` for the full list.

        Must always return an integer. Return 0 for success, or ``-1`` for
        unsupported operations. (Returning 0 for an unhandled operation tells
        the C layer the operation was processed successfully, which may cause
        incorrect behaviour.)
        """
        ...

class StringIO(IO):
    def __init__(self, string: Optional[Any] = None) -> None: ...

class BytesIO(IO):
    """
    In-memory file-like objects for input/output. `StringIO` is used for
    text-mode I/O (similar to a normal file opened with "t" modifier).
    `BytesIO` is used for binary-mode I/O (similar to a normal file
    opened with "b" modifier). Initial contents of file-like objects
    can be specified with *string* parameter (should be normal string
    for `StringIO` or bytes object for `BytesIO`). All the usual file
    methods like ``read()``, ``write()``, ``seek()``, ``flush()``,
    ``close()`` are available on these objects, and additionally, a
    following method:
    """
    def __init__(self, string: Optional[Any] = None) -> None: ...
    def getvalue(self) -> Incomplete:
        """
        Get the current contents of the underlying buffer which holds data.
        """
        ...

def open(name, mode="r", **kwargs) -> Incomplete:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
    ...
