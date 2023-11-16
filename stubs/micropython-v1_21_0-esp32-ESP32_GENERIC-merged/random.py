"""
Module: 'random' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete as Incomplete, Incomplete
from typing import Any, Optional


def randrange(start, stop, step: Optional[Any] = ...) -> int:
    """
    The first form returns a random integer from the range [0, *stop*).
    The second form returns a random integer from the range [*start*, *stop*).
    The third form returns a random integer from the range [*start*, *stop*) in
    steps of *step*.  For instance, calling ``randrange(1, 10, 2)`` will
    return odd numbers between 1 and 9 inclusive.
    """


def random() -> int:
    """
    Return a random floating point number in the range [0.0, 1.0).
    """


def seed(n: Incomplete | None = ...) -> None:
    """
    Initialise the random number generator module with the seed *n* which should
    be an integer.  When no argument (or ``None``) is passed in it will (if
    supported by the port) initialise the PRNG with a true random number
    (usually a hardware generated random number).

    The ``None`` case only works if ``MICROPY_PY_RANDOM_SEED_INIT_FUNC`` is
    enabled by the port, otherwise it raises ``ValueError``.
    """


def uniform(a, b) -> int:
    """
    Return a random floating point number N such that *a* <= N <= *b* for *a* <= *b*,
    and *b* <= N <= *a* for *b* < *a*.
    """


def choice(sequence) -> Incomplete:
    """
    Chooses and returns one item at random from *sequence* (tuple, list or
    any object that supports the subscript operation).
    """


def randint(a, b) -> int:
    """
    Return a random integer in the range [*a*, *b*].
    """


def getrandbits(n) -> int:
    """
    Return an integer with *n* random bits (0 <= n <= 32).
    """
