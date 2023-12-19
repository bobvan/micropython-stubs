"""
Module: 'os' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32S3 module with ESP32S3', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.11.2
from typing import Any


def stat(*args, **kwargs) -> Any:
    ...


def rmdir(*args, **kwargs) -> Any:
    ...


def rename(*args, **kwargs) -> Any:
    ...


def mount(*args, **kwargs) -> Any:
    ...


def mkdir(*args, **kwargs) -> Any:
    ...


def statvfs(*args, **kwargs) -> Any:
    ...


def unlink(*args, **kwargs) -> Any:
    ...


def uname(*args, **kwargs) -> Any:
    ...


def umount(*args, **kwargs) -> Any:
    ...


def urandom(*args, **kwargs) -> Any:
    ...


def chdir(*args, **kwargs) -> Any:
    ...


def dupterm(*args, **kwargs) -> Any:
    ...


def remove(*args, **kwargs) -> Any:
    ...


def listdir(*args, **kwargs) -> Any:
    ...


def dupterm_notify(*args, **kwargs) -> Any:
    ...


def ilistdir(*args, **kwargs) -> Any:
    ...


def getcwd(*args, **kwargs) -> Any:
    ...


class VfsLfs2:
    def rename(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class VfsFat:
    def rename(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...