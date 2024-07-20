"""
Basic "operating system" services.

MicroPython module: https://docs.micropython.org/en/v1.24.0-preview/library/os.html

CPython module: :mod:`python:os` https://docs.python.org/3/library/os.html .

The ``os`` module contains functions for filesystem access and mounting,
terminal redirection and duplication, and the ``uname`` and ``urandom``
functions.

---
Module: 'os' on micropython-v1.21.0-webassembly-GENERIC
"""

from __future__ import annotations

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'webassembly', 'board': 'GENERIC', 'cpu': 'Emscripten', 'mpy': '', 'arch': ''}
# Stubber: v1.15.0
from typing import IO, Iterator, Optional, Tuple, Any
from _typeshed import Incomplete
from stdlib.os import *


def rename(old_path, new_path) -> None:
    """
    Rename a file.
    """
    ...


def rmdir(path) -> None:
    """
    Remove a directory.
    """
    ...


def mount(fsobj, mount_point, *, readonly=False) -> Incomplete:
    """
    See `vfs.mount`.
    """
    ...


def unlink(*args, **kwargs) -> Incomplete: ...


def umount(mount_point) -> Incomplete:
    """
    See `vfs.umount`.
    """
    ...


def stat(path) -> Incomplete:
    """
    Get the status of a file or directory.
    """
    ...


def statvfs(path) -> Tuple:
    """
    Get the status of a filesystem.

    Returns a tuple with the filesystem information in the following order:

         * ``f_bsize`` -- file system block size
         * ``f_frsize`` -- fragment size
         * ``f_blocks`` -- size of fs in f_frsize units
         * ``f_bfree`` -- number of free blocks
         * ``f_bavail`` -- number of free blocks for unprivileged users
         * ``f_files`` -- number of inodes
         * ``f_ffree`` -- number of free inodes
         * ``f_favail`` -- number of free inodes for unprivileged users
         * ``f_flag`` -- mount flags
         * ``f_namemax`` -- maximum filename length

    Parameters related to inodes: ``f_files``, ``f_ffree``, ``f_avail``
    and the ``f_flags`` parameter may return ``0`` as they can be unavailable
    in a port-specific implementation.
    """
    ...


def chdir(path) -> Incomplete:
    """
    Change current directory.
    """
    ...


def mkdir(path) -> Incomplete:
    """
    Create a new directory.
    """
    ...


def remove(path) -> None:
    """
    Remove a file.
    """
    ...


def getcwd() -> Incomplete:
    """
    Get the current directory.
    """
    ...


def listdir(dir: Optional[Any] = None) -> Incomplete:
    """
    With no argument, list the current directory.  Otherwise list the given directory.
    """
    ...


def ilistdir(dir: Optional[Any] = None) -> Iterator[Tuple]:
    """
    This function returns an iterator which then yields tuples corresponding to
    the entries in the directory that it is listing.  With no argument it lists the
    current directory, otherwise it lists the directory given by *dir*.

    The tuples have the form *(name, type, inode[, size])*:

     - *name* is a string (or bytes if *dir* is a bytes object) and is the name of
       the entry;
     - *type* is an integer that specifies the type of the entry, with 0x4000 for
       directories and 0x8000 for regular files;
     - *inode* is an integer corresponding to the inode of the file, and may be 0
       for filesystems that don't have such a notion.
     - Some platforms may return a 4-tuple that includes the entry's *size*.  For
       file entries, *size* is an integer representing the size of the file
       or -1 if unknown.  Its meaning is currently undefined for directory
       entries.
    """
    ...


class VfsPosix:
    """
    See `vfs.VfsPosix`.
    """

    def rename(self, *args, **kwargs) -> Incomplete: ...

    def umount(self, *args, **kwargs) -> Incomplete: ...

    def mount(self, *args, **kwargs) -> Incomplete: ...

    def statvfs(self, *args, **kwargs) -> Incomplete: ...

    def rmdir(self, *args, **kwargs) -> Incomplete: ...

    def stat(self, *args, **kwargs) -> Incomplete: ...

    def remove(self, *args, **kwargs) -> Incomplete: ...

    def mkdir(self, *args, **kwargs) -> Incomplete: ...

    def open(self, *args, **kwargs) -> Incomplete: ...

    def ilistdir(self, *args, **kwargs) -> Incomplete: ...

    def chdir(self, *args, **kwargs) -> Incomplete: ...

    def getcwd(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...
