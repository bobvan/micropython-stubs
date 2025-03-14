"""
Cryptographic ciphers.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/cryptolib.html

---
Module: 'cryptolib' on micropython-v1.21.0-unix-linux_[GCC_9.4.0]_version
"""

from __future__ import annotations

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Optional, Any
from _typeshed import Incomplete


class aes:
    def encrypt(self, in_buf, out_buf: Optional[Any] = None) -> Incomplete:
        """
        Encrypt *in_buf*. If no *out_buf* is given result is returned as a
        newly allocated `bytes` object. Otherwise, result is written into
        mutable buffer *out_buf*. *in_buf* and *out_buf* can also refer
        to the same mutable buffer, in which case data is encrypted in-place.
        """
        ...

    def decrypt(self, in_buf, out_buf: Optional[Any] = None) -> Incomplete:
        """
        Like `encrypt()`, but for decryption.
        """
        ...

    def __init__(self, *argv, **kwargs) -> None:
        """
        Initialize cipher object, suitable for encryption/decryption. Note:
        after initialization, cipher object can be use only either for
        encryption or decryption. Running decrypt() operation after encrypt()
        or vice versa is not supported.

        Parameters are:

            * *key* is an encryption/decryption key (bytes-like).
            * *mode* is:

                * ``1`` (or ``cryptolib.MODE_ECB`` if it exists) for Electronic Code Book (ECB).
                * ``2`` (or ``cryptolib.MODE_CBC`` if it exists) for Cipher Block Chaining (CBC).
                * ``6`` (or ``cryptolib.MODE_CTR`` if it exists) for Counter mode (CTR).

            * *IV* is an initialization vector for CBC mode.
            * For Counter mode, *IV* is the initial value for the counter.
        """
        ...
