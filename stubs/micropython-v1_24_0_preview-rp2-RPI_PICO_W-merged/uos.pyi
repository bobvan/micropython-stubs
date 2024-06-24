"""
Basic "operating system" services.

MicroPython module: https://docs.micropython.org/en/v1.24.0-preview/library/os.html

CPython module: :mod:`python:os` https://docs.python.org/3/library/os.html .

The ``os`` module contains functions for filesystem access and mounting,
terminal redirection and duplication, and the ``uname`` and ``urandom``
functions.

---
Module: 'uos' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.62.g908ab1cec', 'ver': '1.24.0-preview-preview.62.g908ab1cec', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from stdlib.os import *
from typing import Any, IO, Iterator, Optional, Tuple

def rmdir(path) -> None:
    """
    Remove a directory.
    """
    ...

def stat(path) -> Incomplete:
    """
    Get the status of a file or directory.
    """
    ...

def urandom(n) -> bytes:
    """
    Return a bytes object with *n* random bytes. Whenever possible, it is
    generated by the hardware random number generator.
    """
    ...

def rename(old_path, new_path) -> None:
    """
    Rename a file.
    """
    ...

def mount(fsobj, mount_point, *, readonly=False) -> Incomplete:
    """
    See `vfs.mount`.
    """
    ...

def uname() -> uname_result:
    """
    Return a tuple (possibly a named tuple) containing information about the
    underlying machine and/or its operating system.  The tuple has five fields
    in the following order, each of them being a string:

         * ``sysname`` -- the name of the underlying system
         * ``nodename`` -- the network name (can be the same as ``sysname``)
         * ``release`` -- the version of the underlying system
         * ``version`` -- the MicroPython version and build date
         * ``machine`` -- an identifier for the underlying hardware (eg board, CPU)
    """
    ...

def unlink(*args, **kwargs) -> Incomplete: ...
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

def umount(mount_point) -> Incomplete:
    """
    See `vfs.umount`.
    """
    ...

def sync() -> None:
    """
    Sync all filesystems.
    """
    ...

def mkdir(path) -> Incomplete:
    """
    Create a new directory.
    """
    ...

def dupterm(
    stream_object,
    index=0,
) -> IO:
    """
    Duplicate or switch the MicroPython terminal (the REPL) on the given `stream`-like
    object. The *stream_object* argument must be a native stream object, or derive
    from ``io.IOBase`` and implement the ``readinto()`` and
    ``write()`` methods.  The stream should be in non-blocking mode and
    ``readinto()`` should return ``None`` if there is no data available for reading.

    After calling this function all terminal output is repeated on this stream,
    and any input that is available on the stream is passed on to the terminal input.

    The *index* parameter should be a non-negative integer and specifies which
    duplication slot is set.  A given port may implement more than one slot (slot 0
    will always be available) and in that case terminal input and output is
    duplicated on all the slots that are set.

    If ``None`` is passed as the *stream_object* then duplication is cancelled on
    the slot given by *index*.

    The function returns the previous stream-like object in the given slot.
    """
    ...

def chdir(path) -> Incomplete:
    """
    Change current directory.
    """
    ...

def remove(path) -> None:
    """
    Remove a file.
    """
    ...

def dupterm_notify(*args, **kwargs) -> Incomplete: ...
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

def getcwd() -> Incomplete:
    """
    Get the current directory.
    """
    ...

class VfsFat:
    """
    See `vfs.VfsFat`.
    """

    def rename(self, *args, **kwargs) -> Incomplete: ...
    def mkfs(self, *args, **kwargs) -> Incomplete: ...
    def mount(self, *args, **kwargs) -> Incomplete: ...
    def statvfs(self, *args, **kwargs) -> Incomplete: ...
    def rmdir(self, *args, **kwargs) -> Incomplete: ...
    def stat(self, *args, **kwargs) -> Incomplete: ...
    def umount(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def mkdir(self, *args, **kwargs) -> Incomplete: ...
    def open(self, *args, **kwargs) -> Incomplete: ...
    def ilistdir(self, *args, **kwargs) -> Incomplete: ...
    def chdir(self, *args, **kwargs) -> Incomplete: ...
    def getcwd(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class VfsLfs2:
    """
    See `vfs.VfsLfs2`.
    """

    def rename(self, *args, **kwargs) -> Incomplete: ...
    def mkfs(self, *args, **kwargs) -> Incomplete: ...
    def mount(self, *args, **kwargs) -> Incomplete: ...
    def statvfs(self, *args, **kwargs) -> Incomplete: ...
    def rmdir(self, *args, **kwargs) -> Incomplete: ...
    def stat(self, *args, **kwargs) -> Incomplete: ...
    def umount(self, *args, **kwargs) -> Incomplete: ...
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def mkdir(self, *args, **kwargs) -> Incomplete: ...
    def open(self, *args, **kwargs) -> Incomplete: ...
    def ilistdir(self, *args, **kwargs) -> Incomplete: ...
    def chdir(self, *args, **kwargs) -> Incomplete: ...
    def getcwd(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
